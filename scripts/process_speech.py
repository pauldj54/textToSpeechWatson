import csv
from email import charset

with open('c:/Users/pauld/git/textToSpeechWatson/data/speechs.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    data = list(reader)

for row in data:
    #print(row[0] + ' length: ' + str(len(row)))
    print(row[0] + ' - ' + row[1])
    

