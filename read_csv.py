import csv
with open('realEstate.csv') as file:
	reader = csv.reader(file, delimiter=',')

	count=0
	for row in reader:
		print(row[4])

		if count > 5:
		    break

		count +=1
