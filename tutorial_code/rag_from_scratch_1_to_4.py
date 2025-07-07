import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can access environment variables
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2', 'true')
os.environ['LANGCHAIN_ENDPOINT'] = os.getenv('LANGCHAIN_ENDPOINT', 'https://api.smith.langchain.com')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

### IMPORTS ###

import bs4
import numpy as np
import tiktoken

from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate

### PART 1: INDEXING (LOADING, SPLITTING, EMBEDDING) ###

# Load web document
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever()

### PART 2: TOKEN COUNT AND SIMILARITY CHECKING ###

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(string))

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    return dot_product / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Example usage
question = "What kinds of pets do I like?"
document = "My favorite pet is a cat."

query_result = embeddings.embed_query(question)
document_result = embeddings.embed_query(document)
similarity = cosine_similarity(query_result, document_result)
print("Cosine Similarity:", similarity)

### PART 3: RETRIEVAL ###

retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
docs = retriever.get_relevant_documents("What is Task Decomposition?")
print("Retrieved documents:", len(docs))

### PART 4: GENERATION ###

# Manual template prompt
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# LLM setup
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Execute generation
response = (prompt | llm).invoke({"context": docs, "question": "What is Task Decomposition?"})
print("\nResponse:\n", response)

### PART 5: FULL RAG CHAIN ###

prompt_from_hub = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt_from_hub
    | llm
    | StrOutputParser()
)

answer = rag_chain.invoke("What is Task Decomposition?")
print("\nRAG Chain Answer:\n", answer)