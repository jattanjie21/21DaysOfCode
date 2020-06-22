# Why not try a loop today....
#
#
# What’s the minimum number of times you have to flip a coin before you can have
# three consecutive flips that result in the same outcome (either all three are heads or
# all three are tails)? What’s the maximum number of flips that might be needed? How
# many flips are needed on average? 
#
#  
# In this exercise i will explore these questions
# by creating a program that simulates several series of coin flips.



#Just realized i need a method i created yesterday
#Awesome so i just have to import sweet!!
from Day1.day1 import *

import random
minimum = 1
maximum = 2
# the number 1 means head 
# the number 2 means tail

flip_test = 10
# Number of times i will test the script sort of
# Inorder to find the average

list_flips = []

flips = 0
def flip():
    global flips
    flips += 1
    return random.randint(minimum,maximum)

trials = 10000
for i in range(trials):
    first_flip = flip()
    while flip() == first_flip:
        pass

print("flips done is {}".format(flips))
print("average flips", flips / trials)




