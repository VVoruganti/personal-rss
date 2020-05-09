import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

sites = [
        "http://www.reddit.com/r/news",
        "https://news.ycombinator.com/",
        "https://lobste.rs/",
        "https://devpost.com/",
        "https://www.echojs.com",
        "https://www.producthunt.com/"]

options = Options()
options.headless = True

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")

# driver.close()
