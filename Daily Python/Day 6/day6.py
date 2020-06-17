# In this challenge we will write a program to convert an angle
#  from degrees toraidans or from radians to degrees based on 
# the user’s choice. Our program will:

#    Display a menu of options to the end user.
#    Ask the end-user to choose an option from the menu.
#    Ask the end-user to input an angle in the required unit.
#    Calculate and output the angle in the alternative angle unit.

import math

#Converting from radian to degree 
def rad_deg(number):
    degree = number * ( 180 / math.pi )
    return degree

#Converting from degree to radian 
def deg_rad(number):
    radian = number * (math.pi / 180)
    return radian

#Option
def option():
    print("MENU")
    print("A. CONVERT FROM DEGREE TO RADIAN")
    print("B. CONVERT FROM RADIAN TO DEGREES")
    print("C. QUIT")

    choice_input = float(input(">> "))

    if choice_input.lower() == 'a':
        print(deg_rad(choice_input))

    elif choice_input.lower() == 'b':
        print(rad_deg(choice_input))

    elif choice_input.lowe() == 'c':
        exit()
    else:
        print("Wrong input")

#Calling the option method
option()