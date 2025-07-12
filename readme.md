## California Legal RAG project 

The goal of this project is to implement RAG by receving text input from websites containing California Specific Laws to better train the LLM to give accurate legal advice to specific questions.

Initially for this project I had planned on using the BeautifulSoup API to webscrape legal sites on the internet however luckily there exists an API that allows for me to bulk import data into the RAG model. To use this model you have to register but the api is free.
[LegiScan  API](https://api.legiscan.com/docs/) 

I will use LangChain to encode and embed the text from the TextFile into a vector database, which will then be utilized by the RAG (Retrieval-Augmented Generation) model.