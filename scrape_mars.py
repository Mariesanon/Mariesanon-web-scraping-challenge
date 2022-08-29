from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from selenium import webdriver


data_info= {}
def news_data():
     news_url = 'https://redplanetscience.com/'
     driver = webdriver.Chrome()
     driver.get(news_url)
     page_source = driver.page_source
     soup = bs(page_source, 'html.parser')
     data = soup.find("div", class_="content_title")
     data_info['news_data'] = data

     return data_info
     
def scrapping_images():
     image_ul='https://spaceimages-mars.com/'
     driver = webdriver.Chrome()
     driver.get(image_ul)
     page_source = driver.page_source
     soup = bs(page_source, 'lxml')
     data = soup.find("img", class_="headerimage")
     img_src = data.get('src')
     image_url = image_ul + img_src
     data_info['image_url']= image_url

     return data_info

def all_facts_mars():
     all_mars='https://galaxyfacts-mars.com/'
     data_mars=pd.read_html(all_mars)
     df = data_mars[0]
     earth_facts = 'https://galaxyfacts-mars.com/'
     earth_facts_table = pd.read_html(earth_facts)

     mars_df = data_mars[0] 
     mars_df.columns = ['Mars-Earth Comparison', 'Mars']
     earth_df = earth_facts_table[0]
     mars_df['Earth'] = earth_df[1]
     mars_data = mars_df.to_html()
     data_info['mars'] = mars_data
     return data_info


def hemisperical():
     hem_url="https://marshemispheres.com/"
     browser = requests.get(hem_url)
     html = browser.content
     soup = bs(html, 'html.parser')
     full_url = soup.find_all('div', class_='item')
     
     hemisphere_img_urls=[]      
     for x in full_url:
          title = x.find('h3').text
          url = x.find('a')['href']
          browser = requests.get(url)
          html = browser.content
          soup = bs(html, 'html.parser')
          original_img= soup.find('div',class_='downloads')
          hem_url=original_img.find('a')['href']
          img_data=dict({'title':title, 'img_url':hem_url})
          hemisphere_img_urls.append(img_data)
     data_info['hemisphere_img_urls']=hemisphere_img_urls
     return data_info