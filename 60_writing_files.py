#Python writing files (.txt, .json, .csv)


txt_data = "I like pizza"
file_path = "output.txt"

# VYTVOŘENÍ SOUBORU A NAPSÁNÍ TEXTU DO NĚJ (Text = i like pizza, soubor = output.txt)
with open(file=file_path,mode= "w") as file: # w = write, a = append, r = read, x = exclusive creation
    file.write(txt_data)
    print(f"{txt_data} was written to {file_path}")




