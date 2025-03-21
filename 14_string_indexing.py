# indexing = accesing elements of a sequance using [] (indexing operator)
#       [start : end : step]

credit_number = "1234-5678-9012-3456"
#print(credit_number[1]) - vyprintuje 2, pokud není : bere to vždy začátek

#print(credit_number[0: 4]) #Ending - exclusive, Start - inclusive jde i [:4]
#print(credit_number[5: 9])
#print(credit_number[5:])
#print(credit_number[-1])
#print(credit_number[::2]) # python bere že od startu do konce vše = step => každé druhé číslo

# EXERCISE

print(credit_number[-4 :])
print(credit_number[::-1]) #reversne credit number