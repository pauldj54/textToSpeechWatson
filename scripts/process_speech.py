import csv
from email import charset

with open(r'C:\Users\p.hernandez\git\textToSpeechWatson\data\professornet-episode004-2.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    data = list(reader)

for row in data:
    #print(row[0] + ' length: ' + str(len(row)))
    print(row[0] + ' - ' + row[1])
    

