import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://example.com"

# Send an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Print the page title
print("Page Title:", soup.title.string)
