"""
import os

file_path = "/home/Ola/lab/python_lesson/stuff/"  #using absolute file path


if os.path.exists(file_path):
    print(f"The location {file_path} exist")

    if os.path.isfile(file_path):       #using the .isfile() method to check if the file is actaually a file and not a directory
        print("That is a file")
    elif os.path.isdir(file_path):
        print("this is a directory")
else: 
    print("That location doesnt exist")






####writing and outputing files using python (.txt, .json, .csv)



import json
#employees = ["wale", "yusuf", "ola", "tope", "biola"]

employees= {"name": "Ola", 
             "age": 36,
             "job": "System Auditor",}


txt_data = "i like pizza cos its very sweet"

file_path = "/home/Ola/lab/python_lesson/stuff/output.txt"


try:
    with open(file_path, "w") as file:         #the open method () accept 2 parameters file=file_path, and mode ="w" to create a file saved as file
        json.dump(employees, file, indent=3)                              #the dump() method converts a dictionary to a string
        #file.write(employee + value)                    #using the write() method to write our txt_data to the created file
        print(f"our json file: {file_path} was created")
except FileExistsError:
    print("file already except! so please use another mode")
"""

###Reading python files

try:
    file_path = "/home/Ola/lab/python_lesson/stuff/test.txt"

    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("enter only an excel document")
except PermissionError:
    print("You dont have accesss to read this file")