import sys
import requests
from bs4 import BeautifulSoup as bs

try:
	word = sys.argv[1]
except:
	print("Specify a word!")
	exit(-1)


url = "https://www.shabdkosh.com/dictionary/english-hindi/" + word + "/" + word + "-meaning-in-hindi"

try:
	r = requests.get(url)
except:
	print("Check your Connection!")
	exit(-1)	

try:
	soup = bs(r.content, "lxml")
	header = soup.findAll("em")[0].text
	body = soup.findAll( "ol", {"class":"wnol mt-2"})[0]
	meanings = body.findChildren("li")#, recursive=False)	#recursive=False 
except:
	print("Enter any other word")
	exit(-1)

print()
print(word , ":", header)
print()

for (i, meaning) in enumerate(meanings):
	print(  i + 1 , meaning.text )	#meaning.text




