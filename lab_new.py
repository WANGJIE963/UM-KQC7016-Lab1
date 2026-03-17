import requests
from bs4 import BeautifulSoup

# Step 1: Set the new target URL
URL = "http://quotes.toscrape.com/"
page = requests.get(URL)

# Step 2: Parse the content using BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Step 3: Find all quote containers
# In this website, each quote is inside a <div> with class="quote"
quotes = soup.find_all("div", class_="quote")

print("--- Scraped Quotes List ---")
for q in quotes:
    # Step 4: Extract text from <span> and author from <small>
    text = q.find("span", class_="text").text.strip()
    author = q.find("small", class_="author").text.strip()
    
    print(f"Quote: {text}")
    print(f"Author: {author}")
    print("-" * 30)

print("--- Scraping Finished ---")
