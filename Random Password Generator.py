import string
import random

def passwordgenerator(length):
    if length <= 8:
        print("Password length must be greater than 8")
        return None  # Return None if the length is not valid
    else:
        print('''Choose character set for password from these : 
            1. Letters
            2. Digits
            3. Special characters
            4. Exit''')

    characterList = ""

    # Getting character set for password
    while(True):
        choice = int(input("Pick a number "))
        if choice == 1:
            # Adding letters to possible characters
            characterList += string.ascii_letters
        elif choice == 2:
            # Adding digits to possible characters
            characterList += string.digits
        elif choice == 3:
            # Adding special characters to possible characters
            characterList += string.punctuation
        elif choice == 4:
            break
        else:
            print("Please pick a valid option!")

    if not characterList:
        print("No character set chosen, password cannot be generated.")
        return None  # Return None if no character set is chosen
    else:
        password = []

        for i in range(length):
            # Picking a random character from our character list
            randomchar = random.choice(characterList)
            # Appending a random character to password
            password.append(randomchar)

        return "".join(password)  # Return the generated password as a string

# Getting password length
length = int(input("Enter password length: "))
random_password = passwordgenerator(length)
if random_password:
    print("The Random Password Generator is:", random_password)
