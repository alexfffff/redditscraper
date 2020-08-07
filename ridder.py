456 
import csv
import pandas as pd

#this takes the format where all the commments are in one line and splits it based upon people's names


with open('reddit-bigfive2.csv') as file:
    i = 0
    column = ['name','o','c','e','a','text']
    df = pd.read_csv(file,names = column)
    #result = [f(x, y) for x, y in zip(df[''], df['col2'])]
    essentials = df[['name','text']]
    for row in essentials.itertuples():
        splitup = str(row[2]).split('\n\n')
        splitup2 = pd.Series(splitup)
        splitup2.to_csv('folder/' + row[1] + '.csv',header = False) 





    
