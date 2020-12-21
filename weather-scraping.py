"""
Author:  Mitchell Lazarz
Creation Date:  18 September 2020
Version:  Python 3, edited in Google Colab--Jupytor Notebooks
Description:  This script scrapes the National Weather Service website for
current weather condition information of Humidity, Wind Speed, Barometer reading,
Dewpoint, Visibility, and the date and time of the readings for Hyde Park,
Vermont.  The output are the latitude and longitude of Hyde Park and these
weather condition elements that are scraped.
""" 


# Import required libraries
import requests
from bs4 import BeautifulSoup

# Lat/lon in decimal degrees provided for Hyde Park, VT
lat = '44.5965'
lon = '-72.6143'

# Create url for Hyde Park, VT through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate element on page to be scraped
# This element is located within an id tag called current_conditions_detail
# find() locates the element in the BeautifulSoup object
cur_weather_conditions_details = soup.find(id="current_conditions_detail")

# Extract text from the selected BeautifulSoup object using .text
cur_weather_conditions_details = cur_weather_conditions_details.text

# Final Output shows the weather condition details for the lat and long of Hyde Park, VT
# Return scraped information
print('The Current Weather Conditions at '+ lat +  ", " + lon + " are:" + cur_weather_conditions_details)
