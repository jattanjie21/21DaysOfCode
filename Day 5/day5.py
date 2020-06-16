# A SCRIPT THAT WILL CALCULATE MEAN,MEDIAN,MODE AND RANGE
#
#


#Mean
def mean(*args):
    
    #finding the sum of all the numbers
    total_sum = sum(args)
    length = len(args)

    mean = total_sum / length

    return mean

s = mean(23,3,4,5,6,7,8,9,3,67)
print(s)