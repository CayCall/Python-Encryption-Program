import random
import string

username = input("What is your username ?\n")
password = input("What is your password ?\n")

charset = string.punctuation + string.digits + string.ascii_letters
charset= list(charset)

shuffled_charset = charset.copy()

random.shuffle(shuffled_charset)

encryption_dict = dict(zip(charset, shuffled_charset))
print(encryption_dict)
encyptionValue = ""

#Encypt
for char in password:
    if char in encryption_dict:
        encyptionValue += encryption_dict[char]
        print(encyptionValue)
    else:
        encyptionValue += char

print("\nEncrypted password:" + encyptionValue)
