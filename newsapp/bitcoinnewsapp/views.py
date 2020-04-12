from django.shortcuts import render
from django.shortcuts import render
from newsapi import NewsApiClient
import json

def index(request):
    topic=request.get
    newsapi = NewsApiClient(api_key ='b179c498ab7341bab8d52e7bc6b1adbd') 
    top = newsapi.get_everything(q='corona',sources='yahoo,the-verge,cnbc,bloomberg',
language='en',sort_by='relevancy') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
    #return render(request,'news/index.html',{'data':data},content_type="application/json")
    return render(request, 'news/index.html', context ={"mylist":mylist})