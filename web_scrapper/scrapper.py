from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

"""chromedriver = "C:\Python38\Scripts\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)"""
driver = webdriver.Chrome(executable_path=r"C:\Python38\Scripts\chromedriver.exe")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_2774d07d-bceb-4907-8e02-3b99e76309c5_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_7_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L1_view-all&cid=34WHNYFH5V2Y")


content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
for a in soup.findAll('a',href=True, attrs={'class':'_3pLy-c row'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_3tbKJL'})
    rating=a.find('div', attrs={'class':'gUuXy-'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name   ':products,'Price    ':prices,'Rating      ':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')


"""import os
from selenium import webdriver

chromedriver = "C:\Python38\Scripts\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
"""