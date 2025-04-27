# Pythong reading files (.txt, .json, .csv)

file_path = "employees.txt"


with open(file_path, mode="r") as file:#r= read
    content = file.read()
    print(content)