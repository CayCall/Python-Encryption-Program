import random
import string

username = input("What is your username ?\n")
password = input("What is your password ?\n")

password = string.punctuation + string.digits + string.ascii_letters
password = list(password)
key = password.copy()

random.shuffle(key)

encyptionValue = ""

#Encypt
for letter in password:
    newKey = password.index(letter)
    encyptionValue += key[newKey]

print("Encrypted value:" + encyptionValue)

