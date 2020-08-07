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

#this scrapes reddit with the data_reddit_mbti_big_five scores and gets every comment from them 

# replace with your info
reddit = praw.Reddit(client_id = 'M-18X61VZsCoag', 
                     client_secret = 'eUwAfj77GZAEPPMAA-xvu0-w0T4', 
                     username = 'alexfffff2', 
                     password = 'Fairy tail12', 
                     user_agent = 'new solutions for recruitment')

def get_comments_from_pushshift(**kwargs):
    r = requests.get("https://api.pushshift.io/reddit/comment/search/",params=kwargs)
    data = r.json()
    return data['data']