## California Legal RAG project 

The goal of this project is to implement RAG by receving text input from websites containing California Specific Laws to better train the LLM to give accurate legal advice to specific questions.

sites used:
* https://www.calbar.ca.gov/
* https://govt.westlaw.com/calregs/Index?transitionType=Default&contextData=%28sc.Default%29
* https://courts.ca.gov/news-reference/research-data
* https://www.findlaw.com/state/california-law.html
* https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CONS&division=&title=&part=&chapter=&article=I

I do this by utilizing the beautifulSoup library to webscrape the text data to a single text file. From this text file I will the [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) webScraping library to scrape all the cites and sections. 

I will use LangChain to encode and embed the text from the TextFile into a vector database, which will then be utilized by the RAG (Retrieval-Augmented Generation) model.