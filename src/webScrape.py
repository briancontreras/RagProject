#imports request library
from bs4 import BeautifulSoup
import requests
import re

#gets the HTML Doc as a url and prepares it as a text response
def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

def writeToSingleFileWestLaw(soup, fileName):
    #Get  Article section
    for title in soup.find_all('div', class_='co_title'):
        for strong_tag in title.find_all('strong'):
            with open(fileName, 'a',encoding="utf-8") as file:
                ArticleTitle = strong_tag.get_text(strip=True)
                file.write(ArticleTitle + "\n") 
    
    #Get contents of Article
    for text in soup.find_all('div', class_='co_contentBlock co_section'):
        with open(fileName, 'a',encoding="utf-8") as file:
            file.write(str(text.get_text(strip=True)))
    with open(fileName , "a") as file:
        file.write("\n")

def scrapeUrls(urls, textFileName):
    for url in westLawUrls: 
        html_document = getHTMLdocument(url)
        forSoup = BeautifulSoup(html_document, 'html.parser')
        writeToSingleFileWestLaw(forSoup, 'test.txt')

westLawUrls = [
    "https://govt.westlaw.com/calregs/Document/I7A6B47D0FD4311ECBA0CE8BD2C3F45C2?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default)",
    "https://govt.westlaw.com/calregs/Document/ICF14695063E711EDB5569A0BCCCD916B?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default)",
    "https://govt.westlaw.com/calregs/Document/I7F6CE1A34C6611EC93A8000D3A7C4BC3?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default)",
    "https://govt.westlaw.com/calregs/Document/I406861A35A0D11EC8227000D3A7C4BC3?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default)",
    "https://govt.westlaw.com/calregs/Document/I408F98B35A0D11EC8227000D3A7C4BC3?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default)",
    "https://govt.westlaw.com/calregs/Document/I40B3C2835A0D11EC8227000D3A7C4BC3?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default)"
    ]

scrapeUrls(westLawUrls, 'test.txt')
