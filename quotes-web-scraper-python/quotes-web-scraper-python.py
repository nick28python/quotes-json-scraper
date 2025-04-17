import requests  
from bs4 import BeautifulSoup  
import json  

# Step 1: Website se data fetch karo
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Quotes aur Authors extract karo
quotes = soup.find_all("span", class_="text")  
authors = soup.find_all("small", class_="author")  

# Step 3: JSON format me data prepare karo
data = []

for i in range(len(quotes)):
    quote_data = {
        "quote": quotes[i].text,
        "author": authors[i].text
    }
    data.append(quote_data)

# Step 4: JSON file me save karo
with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("JSON file successfully saved!")