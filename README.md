
Web scraping is a technique in Python to extract information from websites. It involves sending HTTP requests, retrieving HTML content, 
and parsing the data you need using libraries like BeautifulSoup, requests, or advanced tools like Selenium. Below is a detailed guide to web scraping in Python:

# Step 1: Understanding Web Scraping
Use Case: Extracting data from a website (e.g., product prices, articles, or weather data).<br>
Legal Considerations: Ensure compliance with the website's robots.txt file and terms of service.

# Step 2: Setting Up Your Environment

**Install Required Libraries:**
pip install requests beautifulsoup4 lxml

**Additional Libraries (Optional):**
pandas: For storing and analyzing scraped data.<br>
selenium: For scraping JavaScript-rendered content.

# Step 3: Sending an HTTP Request**
Use the requests library to fetch the HTML content of the web page.

Example:

import requests

url = "https://example.com"
response = requests.get(url)

**Check if the request was successful**
if response.status_code == 200:
    print("Request successful!")
    print(response.text[:500])  # Print first 500 characters of the HTML
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
    
# Step 4: Parsing HTML with BeautifulSoup
The BeautifulSoup library helps extract structured data from the HTML.

Example:
from bs4 import BeautifulSoup

**Parse the HTML content**
soup = BeautifulSoup(response.text, 'lxml')

**Find specific elements (e.g., title of the page)**
title = soup.title.text
print(f"Page Title: {title}")

**Find all links on the page**
links = soup.find_all('a')
for link in links[:5]:  # Display the first 5 links
    print(link.get('href'))
    
# Step 5: Navigating the HTML Structure

**Find Elements by Tag:**
paragraphs = soup.find_all('p')
for para in paragraphs[:3]:
    print(para.text)
    
**Find Elements by Class or ID:**
specific_element = soup.find('div', class_='example-class')
print(specific_element.text)

# Step 6: Handling Dynamic Content

For JavaScript-rendered pages, use Selenium.
Install Selenium and a WebDriver:

pip install selenium
Download a browser driver (e.g., ChromeDriver).

Example:

from selenium import webdriver

**Set up the WebDriver**
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

**Fetch the page**
driver.get("https://example.com")

**Get page content**
html = driver.page_source

**Use BeautifulSoup for parsing**
soup = BeautifulSoup(html, 'lxml')
print(soup.title.text)

**Close the driver**
driver.quit()

# Step 7: Storing Scraped Data

**Save data to a CSV or JSON file using pandas.**

Example:

import pandas as pd

data = {
    'Title': [title],
    'Links': [link.get('href') for link in links[:5]]
}

df = pd.DataFrame(data)
df.to_csv('scraped_data.csv', index=False)
print("Data saved to scraped_data.csv")

# Step 8: Error Handling

**Error Handling:**
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


