import pandas as pd


# Creating data from scratch 

data = {
     'pineapples': [3, 2, 0, 1],
     
     'mango': [0, 3, 7, 2]
     
 }
 
 #And then pass it to the pandas DataFrame constructor

purchases = pd.DataFrame(data)

#purchases


# Let's have customer names as our index:

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

#purchase

purchases.loc['June']   #finding the location of the customer


#Reading the data with csv

df = pd.read_csv('purchases.csv')

#Reading with JSon

df = pd.read_json('purchases.json')

# Reading with SQLite
df = pd.read_sql_query("SELECT * FROM purchases", con)

#Converting back to a CSV, JSON, or SQL

df.to_csv('new_purchases.csv')

df.to_json('new_purchases.json')

df.to_sql('new_purchases', con)