import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://dealayo.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Website content retrieved successfully!")
    soup = BeautifulSoup(response.content, "html.parser")
else:
    print(f"Failed to fetch website content. Status code: {response.status_code}")
    
refrigerators=[]
offer_section = soup.find_all('div', class_='product-item-info')
 
for product in offer_section:
    title= product.find('a', class_='product-item-link').text.strip() if product.find('a', class_='product-item-link')else "No title"
    price=product.find('span', class_='price').text.strip() if product.find('span', class_='price') else " No price"
    if "Refrigerator" in title:
        refrigerators.append({"Title": title, "Price":price})

df=pd.DataFrame(refrigerators)
df.to_csv("refrigerator_offers.csv", index=False)

print("Data saved to 'refrigerator_offers.csv'")