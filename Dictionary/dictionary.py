'''
Note: Using Python 2 may result in unicode errors
'''

import sys
import requests
from bs4 import BeautifulSoup as bs


url = "https://www.shabdkosh.com/search-dictionary?lc=mr&sl=en&tl=mr&e="

# read the word from the command line arguments and append to the url
try:
    word = sys.argv[1]
    url += word
except:
    print("Specify a word!")
    exit(-1)


# load the website's source code
try:
    r = requests.get(url)
    soup = bs(r.content, "lxml")
except:
    print("You're probably not connected to the internet!")
    exit(-1)


# parse the source to obtain all necessary info
try:
    header = soup.findAll("em")[0].text
    answer_list = soup.findAll("ol", {"class":"wnol mt-2"})[0]
    meanings = answer_list.findChildren("li", recursive=False)
except:
    print("Word not found!")
    exit(-1)


# display the results
print()
print(word + ": " + header)

for (i, meaning) in enumerate(meanings):
    print()
    print(str(i + 1) + ".", meaning.text)


