import requests
import os

def show_actions():

    print("Welcome to the file system!\n"
          "Please press:\n"
          "all -> to see all the files of your filesystem\n"
          "up -> to upload a new file\n"
          "down -> to download a file from the filesystem\n"
          "del -> to delete a file from the filesystem\n"
          "stat -> to see the statistics about the filesystem\n"
          "quit -> to close the application\n\n\n")
    
path = "http://172.16.3.190:8080"

if __name__ == '__main__':
    show_actions()

exit = False
    
while not exit:

    choice = input("Your choice: ")
    
    if choice == "all":
        a = requests.get(path + "/files")
        print(a.text + "\n")
 
    elif choice == "up":
    
        filename = input("Type the name of the file you want to upload: ")
        
        if os.path.exists(filename):
            file = open(filename, 'rb')
            files = { 'file' : file}
            u = requests.post(path + "/files", files = files)
            print(u.text + "\n")
            file.close()
        else:
            print("The file you have chosen does not exist")
    
    elif choice == "down":
        filename = input("Type the name of the file you want to download: ")
        d = requests.get(path + "/files/" + filename)
        if d.text != "Something went wrong while downloading the file" :
            file = open(filename, 'wb')
            file.write(d.content)
            print(d.text + "\n")
            file.close()
        else:
            print(d.text + "\n")
    
    elif choice == "del":
         filename = input("Type the name of the file you want to delete: ")
         d = requests.delete(path + "/files/" + filename)
         print(d.text + "\n")
         
    elif choice == "stat":
        s = requests.get(path + "/statistics")
        print(s.text + "\n")
        
    elif choice ==  "quit":
        exit = True
        
    else:
        print("Wrong input, please retry\n")
        