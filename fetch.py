
import urllib.request

proxy = urllib.request.ProxyHandler({'https': 'proxy.iiit.ac.in:8080'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)




from bs4 import BeautifulSoup
import json
import datetime



def download(url,feed_id):
	print(url)
	with open("app/feed/rawfeed/"+feed_id,'wb') as f:
		f.write(urllib.request.urlopen(url+"?rss").read())
		


		
def initiate():

	file=open("app/feed/feedlist")
	feed_list=json.load(file)
	
	base_url="https://flipboard.com/topic/"


	for i in feed_list:
		feed_id=feed_list[i]
		download(base_url+feed_list[i],feed_id)


def drive():

	sfile=open("app/feed/status.cnf")
	stat=json.load(sfile)

	fetchdate=stat["fetch"]
	if not fetchdate==str(datetime.date.today()):
		print("Initiating...")
		initiate()
		stat["fetch"]=str(datetime.date.today())
		sfile=open("app/feed/status.cnf",'w')
		json.dump(stat,sfile)
	else:
		print("Up-to-date..")


drive()