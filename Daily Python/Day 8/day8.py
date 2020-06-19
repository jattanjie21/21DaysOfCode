#TIME IN PYTHON USING THE ARROW LIBRARY
#
#
#

#Importing the arrow library
import arrow

print("WELCOME TO PYCLOCK")
print("1. World Clock\n2. Get Current Time\n3.Last Seen Feature")

#getting the time information
time_info = arrow.utcnow()

input_option = input(">> ")

if input_option == "1":
    pass

elif input_option == "2":
    pass

elif input_option == "3":
    ask = int(input("When last were you here? "))

    last_seen = time_info.humanize(hours = -(ask))

    print('Last seen was',last_seen)


else:
    pass