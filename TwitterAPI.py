import tweepy
import datetime
import time
import random
from tkinter import *
import PIL

root= Tk()
root.title('Twitter API')
root.geometry("500x250")
root.config(bg='red')

#Keys to be added from Twitter API Authentication
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Main Function of the program
def user_info():
    global md
    md=Tk()
    md.geometry("600x600")
    md.title('Twitter Information')
    md.config(bg='red')
    global info
    info=Entry(md, width=30)
    info.grid(row=2,column=1,pady=(10,20))
    info_label=Label(md,text="Enter Id of Twitter User")
    info_label.grid(row=2,column=0,pady=(10,20),padx=(0,10))
    search_button=Button(md,text="Search for User",command=query)
    search_button.grid(row=4,column=0)    

#Query function to print Details of the User
def query():
    global sp
    sp=str(info.get())
    s=api.get_user(sp)
    s_id=str(s.id)
    s_name=str(s.name)
    scr_name=str(s.screen_name)
    s_location=str(s.location)
    if s_location=="":
        s_location="None"
    s_url=str(s.url)
    s_foll_count=str(s.followers_count)
    s_lis_count=str(s.listed_count)
    s_fav_count=str(s.favourites_count)
    s_number_of_tweets=str(number_of_tweets())
    s_number_of_friends=str(number_of_friends())
    info_label=Label(md,text=s_id)
    info_label.grid(row=5,column=1,padx=(10,0),pady=(10,0))
    info_label=Label(md,text=s_name)
    info_label.grid(row=6,column=1,padx=(10,0),pady=(10,0))
    info_label=Label(md,text=scr_name)
    info_label.grid(row=7,column=1,pady=(10,0))
    info_label=Label(md,text=s_location)
    info_label.grid(row=8,column=1,pady=(10,0))
    info_label=Label(md,text=s_url)
    info_label.grid(row=9,column=1,pady=(10,0))
    info_label=Label(md,text=s_foll_count)
    info_label.grid(row=10,column=1,pady=(10,0))
    info_label=Label(md,text=s_lis_count)
    info_label.grid(row=11,column=1,pady=(10,0))
    info_label=Label(md,text=s_fav_count)
    info_label.grid(row=12,column=1,pady=(10,0))
    info_label=Label(md,text=s_number_of_tweets)
    info_label.grid(row=13,column=1,pady=(10,0))
    info_label=Label(md,text=s_number_of_friends)
    info_label.grid(row=14,column=1,pady=(10,20))
    info_label=Label(md,text="ID:")
    info_label.grid(row=5,column=0,pady=(10,0))
    info_label=Label(md,text="Name:")
    info_label.grid(row=6,column=0,pady=(10,0))
    info_label=Label(md,text="Screen Name:")
    info_label.grid(row=7,column=0,pady=(10,0))
    info_label=Label(md,text="Location:")
    info_label.grid(row=8,column=0,pady=(10,0))
    info_label=Label(md,text="URL:")
    info_label.grid(row=9,column=0,pady=(10,0))
    info_label=Label(md,text="Followers Count:")
    info_label.grid(row=10,column=0,pady=(10,0))
    info_label=Label(md,text="Listed Count:")
    info_label.grid(row=11,column=0,pady=(10,0))
    info_label=Label(md,text="Liked Count:")
    info_label.grid(row=12,column=0,pady=(10,0))
    info_label=Label(md,text="Number Of Tweets:")
    info_label.grid(row=13,column=0,pady=(10,0))
    info_label=Label(md,text="Number Of Friends")
    info_label.grid(row=14,column=0,pady=(10,20))
    del_button=Button(md,text="Close Application",command=close)
    del_button.grid(row=22,column=0,pady=(10,0))
    info.delete(0, END)

#Function to exit the GUI
def close():
    md.destroy()

#Function to tweet a default message
def publictweet():
    if datetime.date.today().weekday() == 0:
        tweettopublish = 'Hi everyone, today is Monday.   #Monday '
    if datetime.date.today().weekday() == 1:
        tweettopublish = 'Enjoy your Tuesday.  #Tuesday'
    if datetime.date.today().weekday() == 2:
        tweettopublish = 'Third week of the Week. #Wednesday'
    if datetime.date.today().weekday() == 3:
        tweettopublish = 'Thursday. I cannot wait for the Weekend'
    if datetime.date.today().weekday() == 4:
        tweettopublish = 'Friday...Finally'
    if datetime.date.today().weekday() == 5:
        tweettopublish = 'Great it is Saturday #weekend #Saturday'
    if datetime.date.today().weekday() == 6:
        tweettopublish = 'Sunday morning...#Weekend #enjoy '
    api.update_status(tweettopublish)

#Twitter Bot
def actual_bot():
    root.destroy()
    text_file = FILE_LOCATION
    def get_upto(fname):
        with open(fname, "r") as fread:
            return str(fread.readline())
    def write_upto(fname, last_id):
        with open(fname, "w") as fwrite:
            fwrite.write(str(last_id))
    def actual_bot1():
        last_seen = get_upto(text_file)
        #id of the first tweet for 'Ankit42203625'= 1290344271124414464
        mentions = api.mentions_timeline(last_seen, tweet_mode = 'extended')
        count=0
        for mention in reversed(mentions):
            tweet = mention.full_text.lower()
            if 'happy birthday' in tweet:
                api.update_status('@' + mention.user.screen_name + ' ' + "Thanks For the wishes!!!", mention.id)
                count+=1
            write_upto(text_file, mention.id)
    while True:
        actual_bot1()
        time.sleep(15)

#Function to find number of tweets
def number_of_tweets():
    info = api.get_user(sp)
    return info.statuses_count

#Function to find number of friends
def number_of_friends():
    info = api.get_user(sp)
    return info.friends_count

#Function to search tweet information
def search_tweet():
    dt=Tk()
    dt.geometry("600x600")
    dt.title('Tweet Information')
    dt.config(bg='red')
    x=info_retweets.get()
    tweet_info=api.get_status(x)
    info_retweets_label=Label(dt,text=tweet_info.text)
    info_retweets_label.grid(row=5,column=1,pady=(10,20),padx=(0,10))
    info_retweets_label=Label(dt,text=tweet_info.retweet_count)
    info_retweets_label.grid(row=6,column=1,pady=(10,20),padx=(0,10))
    info_retweets_label=Label(dt,text="Tweet Information")
    info_retweets_label.grid(row=5,column=0,pady=(10,20),padx=(0,10))
    info_retweets_label=Label(dt,text="Number of Retweets")
    info_retweets_label.grid(row=6,column=0,pady=(10,20),padx=(0,10))
    info_retweets.delete(0, END)
    rt.destroy()

#Function to find number of retweets
def count_number_retweets():#Id=1272479136133627905
    global rt
    rt=Tk()
    rt.geometry("600x600")
    rt.title('Tweet Information')
    rt.config(bg='red')
    global info_retweets
    info_retweets=Entry(rt, width=30)
    info_retweets.grid(row=2,column=1,pady=(10,20))
    info_retweets_label=Label(rt,text="Enter Id of the Tweet")
    info_retweets_label.grid(row=2,column=0,pady=(10,20),padx=(0,10))
    search_button=Button(rt,text="Search for The Tweet",command=search_tweet)
    search_button.grid(row=4,column=0)  

def print_public():
    s=info_tweets.get()
    api.update_status(s)
    info_tweets.delete(0, END)
    
#Function to tweet customized information
def tweet_public():
    global wt
    wt=Tk()
    wt.geometry("600x600")
    wt.title('Tweet Information')
    wt.config(bg='red')
    global info_tweets
    info_tweets=Entry(wt, width=60)
    info_tweets.grid(row=2,column=1,pady=(10,20))
    info_tweets_label=Label(wt,text="Enter Tweet")
    info_tweets_label.grid(row=2,column=0,pady=(10,20),padx=(0,10))
    search_button=Button(wt,text="Tweet",command=print_public)
    search_button.grid(row=4,column=0)
    search_button=Button(wt,text="Exit Application",command=wt.destroy)
    search_button.grid(row=4,column=1)
    search_button=Button(wt,text="Predefined Tweet",command=publictweet)
    search_button.grid(row=4,column=2)

#Starting Window Display of GUI
info_label=Label(root,text="------------------------------Welcome to Twitter API Application--------------------------------")

info_label.grid(row=0,column=0,pady=(10,50))    
view_button = Button(root,text="Information Of A User", command=user_info)
view_button.grid(row=1,column=0,padx=(0,250),pady=(0,20))
current_trends_button = Button(root,text="Initiate Bot", command=actual_bot)
current_trends_button.grid(row=1,column=0,padx=(250,0),pady=(0,20))
count_number_retweets_button = Button(root,text="Retweet Count", command=count_number_retweets)
count_number_retweets_button.grid(row=2,column=0,padx=(0,250),pady=(0,20))
tweet_public_button = Button(root,text="Tweet Publically", command=tweet_public)
tweet_public_button.grid(row=2,column=0,padx=(250,0),pady=(0,20))
destroy_button = Button(root,text="Exit Application", command=root.quit)
destroy_button.grid(row=3,column=0,padx=(10,0),pady=(20,0))

root.mainloop()    
