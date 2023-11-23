import requests
from bs4 import BeautifulSoup
import pandas as pd

# url
url = "https://github.com/topics"

# fetching data from the url
response = requests.get(url)

# making the Soup Object
htmlData = BeautifulSoup(response.text, 'html.parser')
# making it prettify to look it clean
htmlData.prettify()

# fetching the p tags with a specific class name
title_tags = htmlData.find_all('p', {'class': "f3 lh-condensed mb-0 mt-1 Link--primary"})
titles = [title.text for title in title_tags]

# fetching the p tags with a specific class name
description_tags = htmlData.find_all('p', {'class': "f5 color-fg-muted mb-0 mt-1"})
descriptions = [description.text.strip() for description in description_tags]

# fetching the a tags with a specific class name
link_tags = htmlData.find_all('a', {'class': "no-underline flex-1 d-flex flex-column"})
links = ['https://github.com' + link['href'] for link in link_tags]

data = {"Title": titles, "Description": descriptions, "Links": links}
DF = pd.DataFrame(data)
DF.to_csv('Data.csv')
