# Password Generator

# Write a programme, which generates a random password for the user. 
# Ask the user how long they want their password to be, 
# and how many letters and numbers they want in their password. 
# Have a mix of upper and lowercase letters.

from string import ascii_letters, punctuation, digits

from random import randint,choice

class PassGen():

    def __init__(self,user):
        self.user = user
        self.passwords = []

    def generate(self):
        #gen = input("How long do you want your password to be? ")

        min = 15
        max = 20

        string_format = ascii_letters

        generated_string = "".join(choice(string_format) for x in range(randint(min, max)))

        self.passwords.append(generated_string)

        print(generated_string)

new_guy = PassGen("jatta_njie")

new_guy.generate()
