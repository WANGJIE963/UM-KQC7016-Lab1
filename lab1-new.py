import requests
from bs4 import BeautifulSoup

# Step 1: Find the URL and send a request
URL = "http://books.toscrape.com/"
page = requests.get(URL)

# Step 2: Parse the HTML page
soup = BeautifulSoup(page.content, "html.parser")

# Step 3: Find the data you want to extract (Target the container)
# Every book on this site is inside an <article> tag with class="product_pod"
books = soup.find_all("article", class_="product_pod")

print("--- Scraped Books Data ---")

# Step 4 & 5: Extract, clean, and structure the data
for book in books:
    # Extract the title. The title is inside an <a> tag, inside an <h3> tag.
    # We use ['title'] to get the full title attribute, avoiding truncated text.
    title = book.find("h3").find("a")["title"]
    
    # Extract the price. The price is in a <p> tag with class="price_color"
    price_element = book.find("p", class_="price_color")
    price = price_element.text.strip()
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print("-" * 30)

print("--- Scraping Finished ---")
