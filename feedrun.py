from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify
import os


from app.models.feed_mod import Feed
from app import db
import hashlib
import json

mod_feed = Blueprint('feed', __name__)




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
    
    
    
    f_title=f["title"]
    f_summary=f["summary"]
    f_link=f["link"]
    f_image=f["image"]
    f_date=f["date"]
    f_topic=f["topic"]
    f_tag=f["tag"]
    f_hash=hashlib.sha1(f_title.encode('utf8')).hexdigest()
    f_tstamp=timestamp(f_date)


    newfeed=Feed(title=f_title,summary=f_summary,
                link=f_link,image=f_image,date=f_date,
                tag=f_tag,topic=f_topic,hashval=f_hash,    
                time=f_tstamp)

   
    try:
        db.session.add(newfeed)
        db.session.commit()

    except Exception as e:
        #print('error')
        print(e)
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
            if not img[:4]=="http":
                break

            print(img[:4])
            #feed['image']='static/assets/topic/fox.jpg'
            
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



file=open("app/feed/feedlist")
code_list=json.load(file)

code={}
for i in code_list:
    code[code_list[i]]=i

rawfeed_list=os.listdir("app/feed/rawfeed/")


for i in rawfeed_list:
    feeds=readfeeds("app/feed/rawfeed/"+i,code[i])
    print("Saving  ",code[i])
    #print(feeds)
    for j in feeds:
        updateDB(j)
        
    

