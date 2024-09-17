# Web Scraping Climate News from The Guardian

This Python script scrapes climate-related news articles from The Guardian's international page. It extracts titles and summaries of articles and saves this information into a CSV file using pandas.

## Table of Contents
- [Description](#description)
- [Dependencies](#dependencies)
- [Code Explanation](#code-explanation)
- [Usage](#usage)
- [Example](#example)
- [Conclusion](#conclusion)

## Description

The script connects to The Guardian's international news page, parses the HTML content to extract information about climate-related articles, and saves the extracted data into a CSV file. This can be useful for data analysis or tracking climate news over time.

## Dependencies

- Python 3.x
- requests library (for sending HTTP requests)
- beautifulsoup4 library (for parsing HTML)
- pandas library (for data manipulation and CSV export)

You can install the required libraries with:
```
pip install requests beautifulsoup4 pandas
```
## Code Explanation

### 1. Import Libraries
```
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
```
- `requests: For sending HTTP requests to fetch web content.
- BeautifulSoup: For parsing HTML content.
- pandas: For handling and exporting data in CSV format.
- time: For potential use in delaying requests (not used in the current script but commonly used in web scraping).

### 2. Define URL and Send HTTP GET Request

```
url = "https://www.theguardian.com/international"
response = requests.get(url)
```
- `url`: The URL of The Guardian's international page.
- `requests.get()`: Sends an HTTP GET request to the URL to retrieve the page content.

### 3. Parse HTML Content

```
soup = BeautifulSoup(response.content, 'html.parser')
```
- `BeautifulSoup`: Parses the HTML content of the page for further extraction.

### 4. Extract Information

```
climate = []
for row in soup.select('div.dcr-yyvovz'):
    try:
        title = row.find('h3', class_='fc-item__title').get_text(strip=True)
        underLine = row.find('span', class_='fc-item__standfirst').get_text(strip=True)
        climate.append([title, underLine])
    except AttributeError:
        # If any element is not found, skip this row
        continue
```
- `soup.select('div.dcr-yyvovz')`: Selects all `<div>` elements with the class `dcr-yyvovz`.
- Extracts `title` and `underLine` (summary) from each selected element.
- Appends the extracted data to the `climate` list.

### 5. Store Data in a DataFrame

```
df = pd.DataFrame(climate, columns=['title', 'underLine'])
```
- `pandas.DataFrame`: Creates a DataFrame from the `climate` list with columns `title` and `underLine`.

### 6. Export Data to CSV

```
df.to_csv('climate.csv', index=False)
```
- `df.to_csv()`: Exports the DataFrame to a CSV file named `climate.csv` without including the DataFrame index.

## Usage

1. **Install Dependencies**: Ensure you have Python 3.x and the required libraries installed.
2. **Run the Script**: Copy the code into a Python file (e.g., `scrape_climate_news.py`).
3. **Execute the Script**: Run the script using Python:
   
```
   python scrape_climate_news.py
   ```
4. **Check Output**: Verify that the `climate.csv` file has been created in the same directory as the script.

## Example

Running the script will generate a `climate.csv` file containing titles and summaries of climate-related news articles from The Guardian.

## Conclusion

This script provides a simple way to scrape and store climate news data from The Guardian. It demonstrates basic web scraping techniques and data handling using Python libraries.

