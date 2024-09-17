import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website to scrape
url = "https://www.theguardian.com/international"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the relevant information from the HTML code
climate = []
for row in soup.select('div.dcr-yyvovz'):
    try:
        title = row.find('h3', class_='fc-item__title').get_text(strip=True)
        underLine = row.find('span', class_='fc-item__standfirst').get_text(strip=True)
        climate.append([title, underLine])
    except AttributeError:
        # If any element is not found, skip this row
        continue

# Store the information in a pandas dataframe
df = pd.DataFrame(climate, columns=['title', 'underLine'])

# Export the data to a CSV file
df.to_csv('climate.csv', index=False)