#imports request library
from bs4 import BeautifulSoup

#imports request library to process http requests
import requests

#regular expression library, however not needed to be installed since it's part of the python library
import re

#gets the HTML Doc as a url and prepares it as a text response
def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

#constant url can be any url I want to scrape
url_to_scrape = "https://www.geeksforgeeks.org/courses/"
#sets up HTML doc based on the static url
html_document = getHTMLdocument(url_to_scrape)

#calls beautifulSoup library 
soup = BeautifulSoup(html_document, 'html.parser')

# Summary this for loop does: It finds and prints all <a> (anchor) tags in an HTML page whose href attribute starts with "https://".
# for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
#             #finds all anchor tags with the attributes of href that start with https://
#     print(link.get('href'))


url_test = "https://www.geeksforgeeks.org/python/beautifulsoup-scraping-link-from-html/"
html_test = getHTMLdocument(url_test)
testSOUP = BeautifulSoup(html_test,'html.parser')

for div in testSOUP.find_all('div', class_='article-title'):
    print(div.find('h1').get_text(strip=True))