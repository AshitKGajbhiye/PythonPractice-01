from bs4 import BeautifulSoup 
import requests 
page = requests.get("https://www.google.dz/search?q=see") 
soup = BeautifulSoup(page.content) 
links = soup.findAll("a") 
for link in links: 
    if link['href'].startswith('/url?q='): 
        print (link['href'].replace('/url?q=',''))