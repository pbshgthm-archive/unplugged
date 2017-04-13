# -*- coding: utf-8 -*-



def readfeeds(page):
	from bs4 import BeautifulSoup
	import re

	file=open(page)
	file=file.read().replace('media:content','media')

	soup=BeautifulSoup(file,'xml')
	item=soup.find_all('item')
	feeds=[]
	
	for i in item:
		feed={}
		feed['title']=i.title.contents[0]
		feed['link']=i.link.contents[0]
		feed['date']=' '.join(i.pubDate.contents[0].split(', ')[1].split(' ')[:3])
		text=i.description.contents[0]
		feed['image']=str(i.find('media')).split('url=')[-1].split(' ')[0][1:-1]
		
		soup=BeautifulSoup(text,'lxml')
		text=soup.text
		
		clean=re.compile('<.*?>')
		text=re.sub(clean,'',text)
		text=text
	
		
		flag=0
		while(1==1):
			if(len(text)<160):
				break
			text=' '.join(text.split(' ')[:-1])
			flag=1
		if(flag==1):text+=' …'
	
		
		feed['summary']=text
		
		feeds.append(feed)
	return feeds

def jsonsave(content,file):
	import json
	file=open(file,'w')
	file.write((json.dumps(content, ensure_ascii=False)))
	file.close()




feeds=readfeeds('programming.txt')
jsonsave(feeds,'topic-pro')


