#! ./venv/bin python
import requests
from bs4 import BeautifulSoup
import praw
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import re


reddit_links = []
hackernews_links = []
lobster_links = []
manga_links = [] 

def soupify(link):
    r = requests.get(link)
    return BeautifulSoup(r.content, "html.parser")

# Code for Reddit
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                     client_secret=os.getenv('CLIENT_SECRET'),
                     user_agent=os.getenv('USER_AGENT'),
                     username=os.getenv('REDDIT_USERNAME'),
                     password=os.getenv('REDDIT_PASSWORD'))
hot_news_posts = reddit.subreddit('news').hot(limit=15)
for post in hot_news_posts:
    reddit_links.append((post.title, post.url))

# Manga from reddit
manga = ["One Piece",
 "Black Clover",
 "Berserk",
 "Kingdom",
 "My Hero Academia",
 "Boku no Hero Academia",
 "Fire Force", 
 "Attack on Titan",
 "Solo Leveling"]

mangas = ''

# Form regex
for i in range(len(manga)):
    mangas += "(" + manga[i] + ")|" 


manga_regex = re.compile(mangas[:-1], re.IGNORECASE)

manga_posts = reddit.subreddit('manga').hot(limit=100)

for post in manga_posts:
    check = manga_regex.search(post.title)
    if(check != None):
        manga_links.append((post.title, post.url))

# Code for Hacker News
hacker_news = soupify("https://news.ycombinator.com/")
hack_cells = hacker_news.find_all("tr", class_="athing")

# Code for lobste.rs
lobsters = soupify("https://lobste.rs/")
lob_cells = lobsters.find_all("li", class_="story")

for i in range(15):
    hack_link = hack_cells[i].find('a', class_="storylink") # title with the link to the article
    hackernews_links.append((hack_link.text,hack_link.get('href')))
    
    lob_link = lob_cells[i].find('a', class_="u-url")
    lobster_links.append((lob_link.text, lob_link.get('href')))

body = "Reddit\n\n"
for cell in reddit_links:
    body += "Title: {}\nLink: {}\n\n".format(cell[0],cell[1])
body += "\nHackernews\n\n"
for cell in hackernews_links:
    body += "Title: {}\nLink: {}\n\n".format(cell[0],cell[1])
body += "\nLobste.rs\n\n"
for cell in lobster_links:
    body += "Title: {}\nLink: {}\n\n".format(cell[0],cell[1])
body += "\nManga\n\n"
for cell in manga_links:
    body += "Title: {}\nLink: {}\n\n".format(cell[0],cell[1])




#############################################################
####                     Email                           ####
#############################################################
smtp = smtplib.SMTP("smtp.gmail.com", 587)

# Required to setup the server
smtp.ehlo()
smtp.starttls()
user = os.getenv("EMAIL_USERNAME")
# For Gmail this is probably an app password
pswd = os.getenv("EMAIL_PASSWORD")

# Authenticates the user
smtp.login(user, pswd)

target = os.getenv("TARGET") 

source = user   

msg = MIMEText(body, _charset="UTF-8")
msg.set_charset('utf8')
msg['FROM'] = source
msg['To'] = target
msg['Subject'] = Header("Personal RSS",'UTF-8').encode()

# _attach = MIMEText(body.encode('utf-8'), 'html', 'UTF-8')
# msg.attach(_attach)

# For some reason there could not be a space between the \n and the next letter
# Could probably be better by just using triple quote messages
smtp.sendmail(source, target, msg.as_string())

# Closes the server
smtp.quit()
