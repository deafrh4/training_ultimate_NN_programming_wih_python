from bs4 import BeautifulSoup
import requests


#url of the website to scrap
url="http://quotes.toscrape.com"

#send a get request to the website
response =requests.get(url)

#parse the page content
soup=BeautifulSoup(response.text,"html.parser")

#extract quotes
quotes =soup.find_all('span',class_='text')

#print the first 5 quotes
for quote in quotes[:5] :
    print(quote.get_text())
