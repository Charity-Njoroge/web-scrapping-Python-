""""
a python script to download all pdfs from a website
"""
import os
import sys
from bs4 import BeautifulSoup
import requests


# input data, ie the urls where the pdfs are to be downloaded
print("Enter the url to download the pdfs from: ")
url = input()
# input the download path where the pdfs will be downloaded
print("Enter the download path in full for where you want to download the pdfs "
      "to: ")
download_path = input()
try:
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    i = 0
    for tag in soup.find_all('a'):
        i = 0
        # get the extension (splittext) from the last name of the full url
        # (basename). splittext splits the url into filename and the extension,
        # in this case, .pdf which is [1]
        if os.path.splitext(os.path.basename(tag))[1] == '.pdf':
            current = requests.get(tag)
            print("\n[*] Downloading : %s" % (os.path.basename(tag)))
            f = open(download_path + "\\" + os.path.basename(tag), "wb")
            f.write(current.content)
            f.close()
            i += 1
    print("\n[*] Downloading %d of files :" % (i+1))
    choice = input("press any key to exit")

except KeyboardInterrupt:
    print("[*] Exiting .......")
    sys.exit(1)

except:
    print("I don't know the problem but sorry")
    sys.exit(2)
