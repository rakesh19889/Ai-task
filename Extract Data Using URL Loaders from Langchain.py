# data_extraction.py
from langchain.document_loaders import URLLoader

# Define the URL to scrape
url = 'https://brainlox.com/courses/category/technical'

# Use URLLoader to load data from the URL
loader = URLLoader(urls=[url])
documents = loader.load()

# Save the extracted documents for later use
with open('documents.json', 'w') as f:
    f.write(documents.to_json())
