# -*- coding: utf-8 -*-


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext import mutable
from sqlalchemy.orm import sessionmaker
import hashlib
import traceback

import os
import json
import urllib.request



Base = declarative_base()


class Feed(Base):
    __tablename__ = 'feeds'

    fhash = Column(String, primary_key=True)
    tstamp=Column(Integer)
    title = Column(String)
    summary = Column(String)
    link = Column(String)
    image = Column(String)
    date = Column(String)
    tag = Column(String)
    topic = Column(String)
    fid = Column(Integer)
    
 


engine = create_engine('sqlite:///main.db')
Base.metadata.create_all(engine)




def timestamp(date):

	m_dict={"Jan":"01","Feb":"02","Mar":"03",
			"Apr":"04","May":"05","Jun":"06",
			"Jul":"07","Aug":"08","Sep":"09",
			"Oct":"10","Nov":"11","Dec":"12",
			"Sept":"09"}


	temp=date.split()
	day=temp[0].zfill(2)
	month=m_dict[temp[1]]
	year=(temp[2])

	return(int(year+month+day))



def updateDB(f):
	
	
	global count
	
	f_title=f["title"]
	f_summary=f["summary"]
	f_link=f["link"]
	f_image=f["image"]
	f_date=f["date"]
	f_topic=f["topic"]
	f_tag=f["tag"]
	f_hash=hashlib.sha1(f_title.encode('utf8')).hexdigest()
	f_tstamp=timestamp(f_date)


	newfeed=Feed(fid=count,title=f_title,summary=f_summary,
				link=f_link,image=f_image,date=f_date,
				tag=f_tag,topic=f_topic,fhash=f_hash,
				tstamp=f_tstamp)

	Session=sessionmaker(bind=engine)
	session=Session()
	try:
		session.add(newfeed)
		session.commit()
		#print("commited")
		count+=1
	except Exception as e:
		#print(e,'\n')
		#print("error")
		pass



def readfeeds(page,topic):
	
	from bs4 import BeautifulSoup
	import re

	file=open(page)
	file=file.read().replace('media:content','media')

	soup=BeautifulSoup(file,'xml')
	item=soup.find_all('item')
	feeds=[]
	
	for i in item:
		try:		

			feed={}
			title=i.title.contents[0]
			feed['link']=i.link.contents[0]
			feed['date']=' '.join(i.pubDate.contents[0].split(', ')[1].split(' ')[:3])
			text=i.description.contents[0]
			img=str(i.find('media')).split('url=')[-1].split(' ')[0][1:-1]
			#feed['image']= hashlib.sha1(title.encode('utf8')).hexdigest()
			feed['image']=img
			feed['tag']=i.category.contents[0]
			feed['topic']=topic
			soup=BeautifulSoup(text,'lxml')
			text=soup.text
			
			clean=re.compile('<.*?>')
			text=re.sub(clean,'',text)

			
			flag=0
			while(1==1):
				if(len(text)<160):
					break
				text=' '.join(text.split(' ')[:-1])
				flag=1
			if(flag==1):text+=' …'
		
			
			feed['summary']=text


			flag=0
			while(1==1):
				if(len(title)<80):
					break
				title=' '.join(title.split(' ')[:-1])
				flag=1
			if(flag==1):title+=' …'
		
			
			feed['title']=title

			try:
				
				#urllib.request.urlretrieve(img,'static/images/'+feed['image'])
				feeds.append(feed)
				pass
			except:
				
				print("image not found"+img)
			
		except Exception as e:

			#print(e)
			pass
	return feeds


file=open("sys/status")
status=json.load(file)




count=int(status['count'])+1

file=open("sys/feedlist")
code_list=json.load(file)

code={}
for i in code_list:
	code[code_list[i]]=i

rawfeed_list=os.listdir("data/rawfeed/")


for i in rawfeed_list:
	feeds=readfeeds("data/rawfeed/"+i,code[i])
	print("Saving  ",code[i])
	#print(feeds)
	for j in feeds:
		updateDB(j)
		
	


sfile=open("sys/status")
stat=json.load(sfile)

stat["count"]=count-1
sfile=open("sys/status",'w')
json.dump(stat,sfile)


