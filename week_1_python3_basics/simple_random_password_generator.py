# TODO Replicate the random password generator and extend to use numbers, capitals, special characters

import random, string

# generate_password creates a random password of a given length
def generate_password(length):
    password = ""
    ascii_letters = string.ascii_letters
    digits = string.digits


    possible_characters = ascii_letters + digits

    # build a password a random character at a time
    for i in range(length):
        password += random.choice(possible_characters)

    return password

# prompt user for length of password they want to generate
password_length = int(input("Enter number of characters required in password: "))

# generate random password and display to user
print(generate_password(password_length))
