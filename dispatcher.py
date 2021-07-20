from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)

working_nodes = {'172.16.3.226': 0, '172.16.3.180': 0, '172.16.3.197': 0}

@app.route('/files', methods = ['GET'])
def get_files():
    return redirect('http://' + compute_IP() + ':8080/' + request.path, code = 307)

@app.route('/files', methods = ['POST'])
def upload_file():
    IP = compute_IP()
    print(IP)
    working_nodes[IP] += int(request.headers['content-length'])
    print(working_nodes[IP])
    response = redirect('http://' + IP + ':8080/' + request.path, code = 307)
    working_nodes[IP] -= int(request.headers['content-length'])
    print(working_nodes[IP])
    return response

@app.route('/files/<path:filename>', methods = ['GET'])
def download_file(filename):
    return redirect('http://' + compute_IP() + ':8080/' + request.path, code = 307)

@app.route('/files/<path:filename>', methods = ['DELETE'])
def delete_file(filename):
    return redirect('http://' + compute_IP() + ':8080/' + request.path, code = 307)

@app.route('/statistics', methods = ['GET'])
def get_statistics():
    return redirect('http://' + compute_IP() + ':8080/' + request.path, code = 307)

def compute_IP():
    minimum_load = min(working_nodes.values())
    print("Minimum load: " + str(minimum_load))
    possible_IPs = [k for k,v in working_nodes.items() if v == minimum_load]
    print("Available IPs: " + str(possible_IPs))
    selected_IP = random.choice(possible_IPs)
    print("Selected IP: " + selected_IP)
    return selected_IP

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)
