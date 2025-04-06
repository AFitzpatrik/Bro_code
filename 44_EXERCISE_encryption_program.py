import random
import string


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars) #převedení stringu na list
key = chars.copy() #udělá kopii chars a uloží ji nově do proměnné key

random.shuffle(key) #random zamíchá list

#print(f"chars: {chars}")
#print(f"key: {key}")

#ENCRYPTION

plain_text = input("Enter your message to encrypt: ")
cipher_text = ""



for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]    #index vrátí pozici každého symbolu ze seznamu

print(f"Plain text: {plain_text}")
print(f"Encrypted text: {cipher_text}")




#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")
