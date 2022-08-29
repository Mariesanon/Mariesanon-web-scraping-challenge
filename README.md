# Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this assignment, I build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I did.

## Part 1 - Scraping

Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Jupyter Notebook file called `mission_to_mars.ipynb` to complete all scraping and analysis tasks. The following outlines what was scraped.

### NASA Mars News

* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

### JPL Mars Space Images - Featured Image

* Scraped the JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars). Used splinter to navigate the site to find the image url for the current Featured Mars Image.

### Mars Weather

* Scraped the Mars Weather from twitter account [here](https://twitter.com/marswxreport?lang=en).

### Mars Facts

* Scraped the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Scraped the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.


## Part 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create an HTML page that displays all of the information that was scraped from the URLs above.

![firstpage.jpg](Images/firstpage.jpg)
![Lastpage.jpg](Images/lastpage.jpg)

- - -
## Web Application Gallary
![mars1.jpg](Images/mars1.jpg)
![mars2.jpg](Images/mars2.jpg)
![mars3.jpg](Images/mars3.jpg)

# MongoDB
![mongodb.jpg](Images/mongodb.jpg)
## Tech Stack

* Used Requestto navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
* Used Flask as my backend to power up my web application.

* Used Pymongo for CRUD applications for the database. 

* Used Bootstrap to structure the HTML template.

## Author

