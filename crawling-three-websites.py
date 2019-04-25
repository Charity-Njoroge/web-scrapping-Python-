"""
A Python BeautifulSoup script to crawl three different domains and return
the names and full urls of all PDF files on the domains.
"""
from bs4 import BeautifulSoup
import pandas as pd
import requests

# enter the three urls to get pdfs urls from
msg = "Enter the urls to crawl or q to exit"
urls = []
links = []
names = []
for i in range(3):
    urls.append(input("Enter urls\n"))
    for url in urls:
        source = requests.get(url)
        soup = BeautifulSoup(source.content, 'html.parser')
        for link in soup.find_all('a'):
            if link.endswith('pdf'):
                links.append(link.get('href'))
                names.append(link.string)
                pdfs_result = zip(links, names)
                labels = ['names', 'links']
                df = pd.DataFrame.from_records(pdfs_result, columns=labels)
                print(df)


