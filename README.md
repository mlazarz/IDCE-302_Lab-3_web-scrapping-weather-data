# Lab 3 – Web Scraping Weather Data

Webscraping is a process of extracting data from websites.  In this lab, we use webscraping to extract live weather data from the National Weather Service website for a particular location, then display the information.  In order to extract this data, we must inspect the website for the unique id tag for the information desired.  The input of this script is the latitude and longitude of Hyde Park, Vermont, the id tag of the information within the website, and the output is the Humidity, Wind Speed, Barometer reading, Dewpoint, Visibility, and the date and time of the live weather reading. 

## The Code
The flow of this script is as follows:
1. The library BeautifulSoup is imported which contains modules for extracting data from .html.
2. The latitude and longitude for Hyde Park, Vermont are assigned variables.
3. The url for the National Weather Service website containing weather information for Hyde Park is assigned to a variable.  The website url is a string with the latitude and longitude variables concatenated for a valid website destination.
4. Using the get() function, the website contents at the url are assigned to a variable.
5. The website contents are then accessed and parsed by creating a BeautifulSoup object.
6. The id tag element is defined to be scraped.  In this script, id="current_condition_details" is the id that contains the information for Humidity, Wind Speed, Barometer, Dewpoint, Visibility, and date/time of weather reading.  All occurrences of this tag are selected from the website content object.
7. The selected occurrences are then exported as text.
8. The weather information is then printed as a message reading "The Current Weather Conditions at 'lat', 'long' are:" with lat and long being the coordinates of Hyde Park followed by the scraped weather details.

## Coding Issues
I did not have any major issues in creating this script. The BeautifulSoup object assignment and associated methods are a difficult subject to understand.  After revising this code, I have a more full understanding however.

##### Author:  Mitchell Lazarz
##### Creation Date:  18 September 2020
##### Version:  Python 3, coded in Google Colab--Jupytor Notebook
