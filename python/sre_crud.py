# crud operation
from pathlib import Path
import os

def readfielandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfielandfolder()
        name = input("please tell your file name: ")
        p =  Path(name)
        if not p.exists():
            with open(p,'w') as fs:    
                data = input("what you want to write in this file: ")
                fs.write(data)
            print(f"File Created Successful")
        else:
            print("print file already exit.")
    except Exception as err:
        print(f"An error occured as {err}")    

def readfile():
    try:

        readfielandfolder()
        name = input("which file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed Successful.")
        else:
            print("The file does not exit.")
    except Exception as err:
        print(f"An error occured as {err}")


def updatefile():
    try:

        readfielandfolder()
        name = input("Tell which file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of yor file: ")
            print("press 2 for overwriting the data of yor file: ")
            print("press 3 for appending same content in yor file: ")

            res = int(input("tell your respons: "))

            if res == 1:
                name2 = input("tell your new file name: ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p,'w') as fs:
                    data= input("tell what you want to write this is overwride the data: ")
                    fs.write(data)

            if res == 3:
                with open(p,'a') as fs:
                    data= input("tell what you want to write this is overwride the data: ")
                    fs.write("  ",data)

    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:

        readfielandfolder()
        name = input("which file want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
            print("file remove successful.")
        else:
            print("No such file exist")

    except Exception as err:
        print(f"An error occured as {err}")


print("press 1 for creating a file: ")
print("press 2 for reading a file: ")
print("press 3 for updating a file: ")
print("press 4 for deleting file: ")

check = int(input("please tell your resons: "))
if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()