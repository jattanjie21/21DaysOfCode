#TIME IN PYTHON USING THE ARROW LIBRARY
#
#
#

#Importing the arrow library
import arrow

print("WELCOME TO PYCLOCK")
print("1.Get Current Time Information\n2.Last Seen Feature")

#getting the time information
time_info = arrow.utcnow()

input_option = input(">> ")

if input_option == "1":
#Formatting the time from utc()
    info = time_info.format('YYYY-MM-DD HH:mm:ss ZZ')

    print(info)

elif input_option == "2":
    ask = int(input("When last were you here? "))

    last_seen = time_info.humanize(hours = -(ask))

    print('Last seen was',last_seen)

else:
    print("Invalid input!!")