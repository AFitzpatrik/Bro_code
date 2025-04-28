#python file decection
import os

file_path = "stuff/test_detection.txt"  #relative path, když je soubor ve stejném adresáři jako skript

if os.path.exists(file_path):
    print (f"The location '{file_path}' exists")
else:
    print (f"The location '{file_path}' does not exist")
#python file decection
import os

file_path = "stuff/test_detection.txt"  #relative path, když je soubor ve stejném adresáři jako skript
file_path2 = "C:/Users/franc/Desktop/bro.txt" #absolute path, když je soubor v jiném adresáři než skript

if os.path.exists(file_path2):
    print (f"The location '{file_path2}' exists")

    if os.path.isfile(file_path2):
        print("That is a file")

    elif os.path.isdir(file_path2):
        print("That is a directory")
else:
    print (f"The location '{file_path2}' does not exist")
