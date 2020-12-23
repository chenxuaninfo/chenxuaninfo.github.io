import requests
from lxml import etree
import pandas as pd

base_url="https://www.cnblogs.com/alexywt/default.html?page="
articles=pd.DataFrame(columns=('day','title','desc'))

def getArticles(startId,endId):
    for i in range(startId,endId):
        getArticlesFromPage(i)


def getArticlesFromPage(pageId):
    global articles

    url=base_url+str(pageId)

    resp=requests.get(url)
    html=etree.HTML(resp.text)
    days= html.xpath('//div[@class="day"]')
    for day in days:
        article=getArticle(day)
        if not article is None:
            articles=articles.append(article,ignore_index=True)


def getArticle(div_day):
    article_title=div_day.xpath('.//div[@class="postTitle"]/a/text()')[0]
    article_title=article_title.replace("\n","")
    if article_title[:4]=="[置顶]":
        return None

    article_title=article_title.strip()
    day_title=div_day.xpath('.//div[@class="dayTitle"]/a/text()')[0]
    post_desc=div_day.xpath('.//div[@class="postDesc"]/text()')[0]
    post_desc=post_desc.replace("\n","")

    article=pd.Series({
        'day': day_title,
        'title': article_title,
        'desc': post_desc.strip()
    })

    return article



if __name__=='__main__':
    getArticles(1,7)
    print(articles)