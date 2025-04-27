#Python writing files (.txt, .json, .csv)


#txt_data = "I LOVE KEBAB"
#file_path = "output.txt"

'''
# VYTVOŘENÍ SOUBORU A NAPSÁNÍ TEXTU DO NĚJ (Text = i like pizza, soubor = output.txt)

with open(file=file_path,mode= "w") as file: # w = write, a = append, r = read, x = exclusive creation
    file.write(txt_data)
    print(f"{txt_data} was written to {file_path}")
'''


'''
try:
    with open(file=file_path,mode= "x") as file: # w = write, a = append, r = read, x = exclusive creation
        file.write(txt_data)
        print(f"{txt_data} was written to {file_path}")
except FileExistsError:
    print(f"{file_path} already exists")
'''

''''
#APPEND = PŘIDÁ DALŠÍ TEXT DO SOUBORU
try:
    with open(file=file_path,mode= "a") as file: # w = write, a = append, r = read, x = exclusive creation
        file.write("\n" + txt_data)
        print(f"{txt_data} was written to {file_path}")
except FileExistsError:
    print(f"{file_path} already exists")
'''
#---------------------------------------------------------------------------------------------------------

'''
employees = ["John", "Jane", "Doe", "Smith"]
file_path = "employees.txt"

try:
    with open(file=file_path,mode= "w") as file: # w = write, a = append, r = read, x = exclusive creation
        for employee in employees:
            file.write(employee + "\n")
        print(f"{employees} was written to {file_path}")
except FileExistsError:
    print(f"{file_path} already exists")
'''
#---------------------------------------------------------------------------------------------------------
'''
import json
employees = {"name": "Spongebob", "age": 20, "job": "Cashier"}
file_path = "employees.json"

try:
    with open(file=file_path,mode= "w") as file: # w = write, a = append, r = read, x = exclusive creation
        json.dump(employees, file, indent=4) #converutje dictionary na json string to output it
        print(f"json file was created! : {file_path}")
except FileExistsError:
    print(f"{file_path} already exists")
'''
#---------------------------------------------------------------------------------------------------------
#CSV = Comma Separated Values
import json
import csv
file_path = "employees.csv"
employees = [["Name", "Age", "Job"],
             ["Spongebob", 20, "Cook"],
             ["Patrick", 37, "Cashier"],
             ["Sandy", 25, "Scientist"]]

try:
    with open(file=file_path,mode= "w", newline="") as file: # w = write, a = append, r = read, x = exclusive creation
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file was created! : {file_path}")
except FileExistsError:
    print(f"{file_path} already exists")
