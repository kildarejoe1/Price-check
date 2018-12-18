__author__="Henry Morrin"

import requests
from bs4 import BeautifulSoup

request=requests.get("https://cloud.servecentric.com/")
content=request.content
print(type(content))
soup=BeautifulSoup(content,"html.parser")

#Need to retrieve data from html returned
