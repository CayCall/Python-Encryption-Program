import random
import string
from time import sleep

username = input("What is your username ?\n")
print("Your username has been saved!")
password = input("What is your password ?\n")
print("Your password is now being saved and encrypted!")
sleep(1)
print("Encrypting...")
sleep(2)

charset = string.punctuation + string.digits + string.ascii_letters
charset= list(charset)

shuffled_charset = charset.copy()

random.shuffle(shuffled_charset)

encryption_dict = dict(zip(charset, shuffled_charset))
encyptionValue = ""

#Encypt
for char in password:
    if char in encryption_dict:
        encyptionValue += encryption_dict[char]
    else:
        encyptionValue += char

print("\nEncrypted password:" + encyptionValue)
