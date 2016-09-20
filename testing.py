import csv
listylist =[["hello","hi"],["bonjour"]]
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                             quoting=csv.QUOTE_MINIMAL)
    for row in listylist:
   	 spamwriter.writerow(row)
   