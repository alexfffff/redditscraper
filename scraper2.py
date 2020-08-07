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

#this scrapes reddit with the savepath scores and gets every comment from them 

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

def get_comments_from_reddit_api(comment_ids):
    headers = {'User-agent':'Comment Collector'}
    params = {}
    params['id'] = ','.join(["t1_" + id for id in comment_ids])
    r = requests.get("https://api.reddit.com/api/info",params=params,headers=headers)
    data = r.json()
    return data['data']['children']

#declarations
subreddit_percentages = {}
save_path = 'reddit-bigfive3.csv'
f = open('data.csv')
csv_f = csv.reader(f)
first = True 

with open(save_path, mode='a+', encoding='utf-8') as file:  
    writer = csv.writer(file)
    for row in csv_f:
        if first:
            first = False
        else:
            before = None
            author = row[0] 
            if author != '[deleted]':
                totalcomment = ''
                while True:
                    try:
                        comments = get_comments_from_pushshift(author=author,size=100,before=before,sort='desc',sort_type='created_utc')
                        if not comments: break

                        # This will get the comment ids from Pushshift in batches of 100 -- Reddit's API only allows 100 at a time
                        comment_ids = []
                        for comment in comments:
                            before = comment['created_utc'] # This will keep track of your position for the next call in the while loop
                            comment_ids.append(comment['id'])

                        # This will then pass the ids collected from Pushshift and query Reddit's API for the most up to date information
                        
                        comments = get_comments_from_reddit_api(comment_ids)
                        for comment in comments:
                            comment = comment['data']
                            # Do stuff with the comments

                            if len(comment['body']) > 100:

                                #writes the row in the file 
                                writer.writerow([author,row[1],row[2],row[3],row[4],row[5],comment['subreddit'],comment['body']])
                                print(comment['body'])

                                #puts the subreddit into the dict
                                if subreddit_percentages.__contains__(comment['subreddit']):
                                    subreddit_percentages[comment['subreddit']] = subreddit_percentages[comment['subreddit']] + 1
                                else:
                                    subreddit_percentages[comment['subreddit']] = 1
                                
                            
                    except Exception as e:
                        print(e) 

print(subreddit_percentages)
        

                
                
                




    # I'm not sure how often you can query the Reddit API without oauth but once every two seconds should work fine
# with open(save_path,mode= 'a+') as file:
#     csv_f = csv.reader(file)
#     first = True 
#     for row in csv_f:
#         if first:
#             first = False
#         else:
#             print row[0] 
        
# user = r.get_redditor('im14')
# for comment in user.get_comments(limit=None):
#     print comment.bodyl