#imports request library
from bs4 import BeautifulSoup
import requests
import re

#gets the HTML Doc as a url and prepares it as a text response
def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

def writeToSingleFile(soup, fileName):
    for text in soup.find_all('pre'):
        with open(fileName, "w") as file:
            file.write(str(text.get_text(strip=True)))


url_to_scrape = "https://www.govinfo.gov/content/pkg/PLAW-119publ1/html/PLAW-119publ1.htm"
html_document = getHTMLdocument(url_to_scrape)
testSOUP = BeautifulSoup(html_document,'html.parser')

writeToSingleFile(testSOUP,'test.txt')