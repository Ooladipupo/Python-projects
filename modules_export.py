
import builtins
import os

modules = dir(builtins)

file_path = "/home/Ola/lab/python_lesson/stuff/modules.txt"

with open(file_path, "w") as file:
    for modul in modules:
        file.write(modul + "\n")