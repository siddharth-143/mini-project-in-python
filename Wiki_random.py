"""
    Python program to get random wikipedia articles.
"""

from bs4 import BeautifulSoup
import requests

# Trying to open a random wikipedia article
# Special : Random open random articles

res = requests.get("https://en.wikipedia.org/wiki/Special:Random")
res.raise_for_status()

# pip install htmlparser
wiki = BeautifulSoup(res.text, "html.parser")

r = open("random_wiki.txt", "w+", encoding="utf-8")

# Adding the heading to the text file
heading = wiki.find("h1").text

r.write(heading + "\n")
for i in wiki.select("p"):
    # Optional printing of text
    # print(i.getText())
    r.write(i.getText())


r.close()
print("File saved as random_wiki.txt")