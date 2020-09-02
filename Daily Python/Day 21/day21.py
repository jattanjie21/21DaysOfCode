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