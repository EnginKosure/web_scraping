import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.ebay.com/"

my_content = requests.get(link)

soup = BeautifulSoup(my_content, 'html.parser')
