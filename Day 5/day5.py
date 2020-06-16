# A SCRIPT THAT WILL CALCULATE MEAN,MEDIAN,MODE AND RANGE
#
#

import 
#Mean
def mean(*args):
    #finding the sum of all the numbers
    total_sum = sum(args)

    length = len(args)

    mean = total_sum / length

    return mean

#Median
def median(*args):
    N = len(args)   #finding the lenght of numbers arguments

    #if the length is even then you add the two mid numbers and divide by 2
    if N % 2 == 0:
        m1 = N / 2  # First middle number

        m2 = (N / 2) + 1

        median = (m1 + m2) / 2

    else:
        median = (N + 1) / 2

    return median

#Mode
def mode(*args):


#s = mean(23,3,4,5,6,7,8,9,3,67)
#print(s)