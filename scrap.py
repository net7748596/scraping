# importation des packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
url="http://feeds.bbci.co.uk/news/rss.xml"
reponse=requests.get(url)
soup=BeautifulSoup(reponse.text,"html.parser")
print(soup)
items=soup.findAll('item')
item=items[0]
item.description.text
news_items=[]

for i in items:
    news_i={}
    news_i['title']=i.title.text
    news_i['description']=i.description.text
    news_i['pubdate']=i.pubdate.text
    news_items.append(news_i)
   
print(news_i)
print(news_items)

# avec le df on a la transformation en base de données
df=pd.DataFrame(news_items,columns=['title','description','pubdate'])

df.head()

df.head(20)

# ébauche du fichier csv

df.to_csv('web_scrapping.csv',index=False,encoding='utf-8')

