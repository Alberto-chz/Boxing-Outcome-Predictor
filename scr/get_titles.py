import httpx
from bs4 import BeautifulSoup

# Target URL
url = 'https://box.live/boxers/vasyl-lomachenko/' 

# Fetching content from page
response = httpx.get(url)

# Parsing HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting title and its content
page_title = soup.find('title').text

# Print the extracted title
print("Page Title:", page_title)
