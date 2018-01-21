# Decode a Web Page

import requests
from bs4 import BeautifulSoup


url = "http://www.nytimes.com/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

for s in soup.find_all("a"):
    print(s.get("href"))

