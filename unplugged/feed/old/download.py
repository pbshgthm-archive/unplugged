
import urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]
from bs4 import BeautifulSoup
import json

url="'https://flipboard.com/topic/programming"
url="https://flipboard.com/@theverge"

def download(url):
	with open("dow_pg",'wb') as f:
		f.write(urllib2.urlopen(url+"?rss").read())
		
download(url)

