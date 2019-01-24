import requests
from bs4 import BeautifulSoup

print("Please enter your Research's title:")
title = input("")
print("Please enter the url of the website:")
url = input("")

r = requests.get(url)
soup = BeautifulSoup(r.text)
info = ""

for p in soup.find_all('p'):
    print(p.text)
    info += p.text

file = open("Research.txt", "w", encoding='utf-8')
file.write(title)
file.write("")
file.write(info)
file.close()