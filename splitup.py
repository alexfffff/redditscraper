456 
import csv
import pandas as pd

with open('reddit-nombti.csv') as file:
    reader = csv.reader(file)
    username = '[deleted]'
    content = []
    for row in reader:
        if username != row[0]:
            content = pd.Series(content)
            content.to_csv('nombti/' + username + '.csv',header = False) 
            username = row[0]
            content = []
            content.append(row[7])
        else:
            content.append(row[7])