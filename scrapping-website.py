from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request


source = requests.get("https://pythonprogramming.net/parsememcparseface/")
soup = BeautifulSoup(source.content, 'html.parser')
for paragraph in soup.find_all('p'):
    print(str(paragraph.text))
for url in soup.find_all('a'):
    print(url.get("href"))
nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)
for div in soup.find_all('div', class_="body"):
    print(div.text)

# find the first table and return it
table = soup.find('table')
# find the rows in the table ie tag tr
table_rows = table.find_all('tr')
# find the table data in each row and store each row's data in a list
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]  # list comprehension
    print(row)
# using pandas
dataframes = pd.read_html("https://pythonprogramming.net/parsememcparseface/")
for df in dataframes:
    print(df)

# parsing XML
source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').\
    read()
soup = BeautifulSoup(source, 'xml')

for url in soup.find_all('loc'):
    print(url.text)