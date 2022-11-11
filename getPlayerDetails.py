from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
session = HTMLSession()
url = "https://oracleselixir.com/player/Airawn/"
response = session.get(url)

response.html.render()
soup = BeautifulSoup(response.html.raw_html, 'html.parser')
print(soup.find_all("div"))

# import requests
# response = requests.get("https://oe.datalisk.io/players/gameDetails/Airawn")

# print(response.text)