


import json
import sys
import os
f_name=sys.argv[1]
print("Getting page...")

url="http://www.theverge.com/2017/2/22/14703712/tesla-supercharger-growth-model-usa-canada-mexico"
api = 'https://mercury.postlight.com/parser?url='+url

import requests
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
r=requests.get(api,headers={'Content-Type': 'application/json','x-api-key': 'ug18NBn4ktmQ4p8xK3S3roIlCdMCVR5TfLBkb02H'})


article=r.json()
for i in article:
	print(i)

#url
#date_published
#title
#lead_image_url
#excerpt
#author
#content







#for i in article:
#	print(i,article[i])
