from flask import Flask
from flask import request
import rados

app = Flask(__name__)

pool = 'data'

def connect():
    cluster = rados.Rados(conffile = './ceph.conf')
    cluster.connect()
    print("Connected to " + cluster.conf_get("mon host"))
    return cluster

def disconnect(cluster):
    cluster.shutdown()

@app.route('/files', methods=['GET'])
def get_files():
    cluster = connect()
    response = ""

    try:
        ioctx = cluster.open_ioctx(pool)
        for file in ioctx.list_objects():
            response += file.key + "\n"

    except Exception as e:
        print(e)
        response = "Something went wrong while retrieving the list of files"

    finally:
        ioctx.close()

    disconnect(cluster)

    return response

@app.route('/files/<path:filename>', methods=['GET'])
def download_file(filename):
    cluster = connect()

    try:
        ioctx = cluster.open_ioctx(pool)
        response = ioctx.read(filename)

    except Exception as e:
        print(e)
        response = "Something went wrong while downloading the file"
    finally:
        ioctx.close()

    disconnect(cluster)

    return response

@app.route('/files', methods=['POST'])
def upload_file():
    cluster = connect()
    file = request.files['file']
    name = file.filename
    body = file.read()

    try:
        ioctx = cluster.open_ioctx(pool)
        outcome = ioctx.write_full(name, body)

        if outcome == 0:
            response = "File successfully uploaded"
        else:
            response = "Something went wrong while uploading the file"

    except Exception as e:
        print(e)
        response = "Something went wrong while uploading the file"

    finally:
        ioctx.close()

    disconnect(cluster)

    return response

@app.route('/files/<path:filename>', methods = ['DELETE'])
def delete_file(filename):
    cluster = connect()

    try:
        ioctx = cluster.open_ioctx(pool)
        outcome = ioctx.remove_object(filename)
        if outcome:
            response = "File successfully deleted"
        else:
            response = "Something went wrong while deleting the file"

    except Exception as e:
        print(e)
        response = "Something went wrong while deleting the file"

    finally:
        ioctx.close()

    disconnect(cluster)

    return response

@app.route('/statistics', methods=['GET'])
def get_statistics():
    cluster = connect()
    response = "Statistics:\n"

    try:
        ioctx = cluster.open_ioctx(pool)
        statistics = ioctx.get_stats()

        for key, value in statistics.items():
            response += str(key) + " --> " + str(value) + "\n"

    except Exception as e:
        print(e)
        response = "Something went wrong while retrieving the statistics"

    finally:
        ioctx.close()

    disconnect(cluster)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)
