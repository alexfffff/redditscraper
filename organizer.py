import praw
import requests
import csv
import json
import os
from tqdm import tqdm
import time
import re
import pandas
import nltk
#this takes reddit-bigfive.csv and splits it up into no mbti and only mbti by excluding subreddits and by not includng comments with the big 5 trait
totalmbti = 0
total = 0
def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
nono = {"mbti","ISTJ","isfj","infj","intj","istp","isfp","infp","INTP","estp","ESFP","ENFP","entp","estj","esfj","enfj","entj","INTPGaming","XNTP",'infjhome','HealthyINTJ','INFJmusic','INFPMemes','INTJmemes','INTPwriting','ESTJ2','INTxx','INFJ_Support_Group','MBTIPlus','my_mbti_type','CandidMBTI','2X__INTP','enneagram','BigFive'}
bigfive = ['openness','extraversion','neuroticism','agreeableness','conscientiousness']
with open('reddit-nombti.csv',mode = 'w') as nombti:
    with open('reddit-onlymbti.csv',mode = 'w') as mbti:
        with open('reddit-bigfive.csv', mode = 'r') as file:
            reader = csv.reader(file)
            writermbti = csv.writer(mbti)
            writernombti = csv.writer(nombti)
            for row in reader:
                if row[6] in nono or any(findWholeWord(x)(row[7]) for x in bigfive):
                    writermbti.writerow(row)
                else:
                    writernombti.writerow(row)
                    

        
            


print(nono)

