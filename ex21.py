# Write to a File

import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

with open("data/monica.txt", "w") as file:
    for s in soup.find_all("p"):
        file.write(s.text)
