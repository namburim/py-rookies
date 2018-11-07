#import csv
#with open('realEstate.csv') as file:
#	reader = csv.reader(file, delimiter=',')
#
#	count=0
#	for row in reader:
#		print(row[4])
#
#		if count > 5:
#		    break
#
#		count +=1

import pandas as pd

df = pd.read_excel("realEstate.xlsx")

inc_price = df.sort_values(["price"], ascending = True)
#inc_price.to_excel("incprice.xlsx", index = False)
1
#count = 0
mylist = []

for index, row in df.iterrows():
    if row['price'] < 100000 and row['beds'] > 1 and row['baths']>1:
        print(row['price'], index)
#        count +=1
        mylist.append(index)
        
#print(count)
#print(mylist)

reqdf = df.take(mylist)
reqdf.to_excel("reqlist.xlsx", index = False)

    
    
    