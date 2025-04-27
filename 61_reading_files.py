# Pythong reading files (.txt, .json, .csv)
import json
#file_path = "employees.txt"

'''
try:
    with open(file_path, mode="r") as file:#r= read
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"{file_path} was not found")
except PermissionError:
    print(f"{file_path} has limited access to read it")
'''
#---------------------------------------------------------------------------------------------------------
#JSON
'''
file_path = "employees.json"
try:
    with open(file_path, mode="r") as file:#r= read
        content = json.load(file)
        print(content["name"])
        #print(content) # přečte vše
except FileNotFoundError:
    print(f"{file_path} was not found")
except PermissionError:
    print(f"{file_path} has limited access to read it")
    '''
#---------------------------------------------------------------------------------------------------------
#CSV
import csv
file_path = "employees.csv"

try:
    with open(file_path, mode="r") as file:#r= read
        content = csv.reader(file)
        for line in content:
            #print(line[0])
            print(line)
except FileNotFoundError:
    print(f"{file_path} was not found")
except PermissionError:
    print(f"{file_path} has limited access to read it")


