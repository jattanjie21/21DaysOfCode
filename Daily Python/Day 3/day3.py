 #Guess The Number

#Write a programme where the computer randomly generates a number between 0 and 20. 
#The user needs to guess what the number is. If the user guesses wrong, 
#tell them their guess is either too high, or too low. 
#This will get you started with the random library if you haven't already used it.

import random

def number_guesser():
    tries = int(input("How many tries do you need incase? "))
    my_guess = int(input("Guess a "))
    guesses = 0

    while guesses <= tries:
        random_number = random.randrange(0,21)
        if random_number == my_guess:
            print("Bravo!!!!!!!!")
            break
        elif random_number < my_guess:
            print(guesses,"attempt wrong, Guess was too low")
        elif random_number > my_guess:
            print(guesses,"attempt wrong, Guess was too high")
        else:
            print()

        guesses += 1

    print("END OF PROGRAM!!!!!!")






