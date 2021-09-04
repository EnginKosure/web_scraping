import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.ebay.com/e/fashion/bo7-omega-021720"

my_content = requests.get(link)

soup = BeautifulSoup(my_content, 'html.parser')

ul = soup.find(
    'ul', attrs={'class': 'b-list__items_nofooter srp-results srp-grid'})


titles = []
prices = []
shippings = []
urls = []

for items in ul.findAll('li', attrs={'class': 's-item'}):
    items.find('h3', attrs={'class': 's-item__title'})
