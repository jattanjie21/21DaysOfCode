#A simple library that prettify data

from prettytable import PrettyTable

#Creating your table
table = PrettyTable()

#Creating field names
table.field_names = ['Name', 'Age', 'Address']


#Function that adds data to the table
def add_record(name,age,address):
    table.add_row([name, age, address])

#Align function
def align_table(position):
    table.align() = position
    
