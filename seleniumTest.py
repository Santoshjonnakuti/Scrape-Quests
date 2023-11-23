# importing necessary modules

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Setting options for Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chromeDriver = webdriver.Chrome(options=options)

# To store data of all 5 Quests
data = []


# Loop to get data of 5 Quests
for i in range(5):
    # Dictonary to store data of a single quest
    record = {}
    
    # Setting up the chrome driver
    chromeDriver.get("https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787")
    # Waiting to load the webpage to ignore errors
    chromeDriver.implicitly_wait(10)
    
    # Getting the main table of
    table = chromeDriver.find_element(by=By.CLASS_NAME, value='datatable')
    
    # Getting table body
    tableBody = table.find_element(by=By.TAG_NAME, value='tbody')
    
    # Getting all available rows in the table body
    tableRows = tableBody.find_elements(by=By.TAG_NAME, value='tr')

    # Finding the necessary td tag to get the link 
    tableData = tableRows[i].find_elements(by=By.TAG_NAME, value='td')
    
    # Finding the a tag of the particular quest
    aTag = tableData[1].find_element(by=By.TAG_NAME, value='a')
    
    # Adding the Quest number to the record
    record['Quest Number'] = tableData[1].text
    
    # Fetching the Data of that particular quest
    aTag.click()
    
    # Waiting for some time to ignore rendering issues
    chromeDriver.implicitly_wait(10)
    
    # Finding the main component which consists data
    divPannelTags = chromeDriver.find_elements(by=By.CLASS_NAME, value='panel')
    
    # Required data is there in 1 and 2 div tags
    divPannelTags = divPannelTags[1:3]
    
    # To get Closing Date and Est. Value Notes
    div = divPannelTags[0]
    tableRowTags = div.find_elements(by=By.TAG_NAME, value='tr')
    
    # To get Closing Date
    tableDataTags = tableRowTags[0].find_elements(by=By.TAG_NAME, value='td')
    record[tableDataTags[0].text[:-1]] = tableDataTags[1].text 
    
    # To get Est. Value Notes
    tableDataTags = tableRowTags[2].find_elements(by=By.TAG_NAME, value='td')
    record[tableDataTags[0].text[:-1]] = tableDataTags[1].text 
    
    # To get Description
    div = divPannelTags[1]
    tableRowTags = div.find_elements(by=By.TAG_NAME, value='tr')
    
    # To get Description
    tableDataTags = tableRowTags[2].find_elements(by=By.TAG_NAME, value='td')
    record[tableDataTags[0].text[:-1]] = tableDataTags[1].text 
    
    # Appending the record to the data
    data.append(record)

# Creating a DataFrame and exporting it into csv
df = pd.DataFrame(data)
df.to_csv("./Data.csv")
    