# -*- coding: utf-8 -*-

def getfeed(url,id):
	import feedparser
	from bs4 import BeautifulSoup
	data=feedparser.parse(url)
	feeds=[]
	print data
	for i in data.entries:
		story={}
		#story["id"]=id+'.'+''.join(i.published.split(',')[1].split(' ')[1:4])+'.'+str(data.entries.index(i))
		story['title']=i.title.encode('utf8')
		story['summary']=i.summary.encode('utf8')
		story['date']=i.published.encode('utf8')
		story['link']=i.link.encode('utf8')
		soup=BeautifulSoup(i.summary,'lxml').encode('utf8')
		try:
			story['image']=soup.img['src'].encode('utf8')
		except:
			story['image']="NIL".encode('utf8')
		feeds.append(story)
	return feeds

	file.close()
def jsonsave(content,file):
	import json
	file=open(file,'w')
	file.write((json.dumps(content, ensure_ascii=False)))


verge="http://www.theverge.com/rss/index.xml"
mit="https://www.technologyreview.com/topnews.rss"
wired="https://www.wired.com/feed/"
flip_design="https://flipboard.com/section/design-hppel0f1ehmnimui?rss"
feeds=getfeed('index.xml','verge')
jsonsave(feeds,"verge")


import urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]

