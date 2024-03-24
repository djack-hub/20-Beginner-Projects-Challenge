#Step 1: Ask user if they want to generate a random password
#Step 2: If yes, ask for the length of the password
#Step 3: Generate the password and show it to the user
#Step 4: if no, exit the program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")  #specifies which characters the random password will be selected from 
    
def generate_password():
    length = int(input("How many characters do you want the password to be?"))

    random.shuffle(characters)
    password = []

    for x in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

prompt = input("Do you want to generate a password?")

if prompt == "Yes":
    generate_password()
elif prompt == "No":
    quit()
else:
    print("Invald Response :( Please enter 'Yes' or 'No'")
    quit()
