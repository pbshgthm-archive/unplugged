
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]
from bs4 import BeautifulSoup
import json



base_url="'https://flipboard.com/topic/"

def download(url,feed_id):
	with open("data/raw_feed"+feed_id,'wb') as f:
		f.write(urllib.request.urlopen(url+"?rss").read())
		


file=open("sys/feedlist")
feed_list=json.load(file)

ind=1
for i in feed_list:
	for j in feed_list[i]:
		feed_id=i+str(ind)
		download(j,feed_id)


