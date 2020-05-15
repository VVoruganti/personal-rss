import requests
from bs4 import BeautifulSoup
import praw

sites = [
        "http://www.reddit.com/r/news",
        "https://news.ycombinator.com/",
        "https://lobste.rs/"]

def soupify(link):
    r = requests.get(link)
    return BeautifulSoup(r.content, "html.parser")

reddit_links = []
hackernews_links = []
lobster_links = []
# Code for Hacker News
hacker_news = soupify(sites[1])
cells = hacker_news.find_all("tr", class_="athing")

for i in range(15):
    link = cells[i].find('a', class_="storylink") # title with the link to the article
    hackernews_links.append((link.text,link.get('href')))

# Code for lobste.rs
lobsters = soupify(sites[2])
cells = lobsters.find_all("li", class_="story")

for i in range(15):
    link = cells[i].find('a', class_="u-url")
    lobster_links.append((link.text, link.get('href')))

# Code for Reddit

