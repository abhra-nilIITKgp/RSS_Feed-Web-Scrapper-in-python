import requests
from bs4 import BeautifulSoup

r=requests.get("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
data=r.text
soup=BeautifulSoup(data, 'html.parser')
p=soup.find_all('description')[1:]
q=soup.find_all('title')[2:]
for i in range(len (q)):
	print(q[i].get_text())
	#print(p[i].get_text())

