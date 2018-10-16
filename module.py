# coding:utf-8
import requests
import json
import os

def return_news(words):
    payload = {
        'country' : 'jp',
        'apiKey' : os.environ['NEWS_API_KEY']
    }
    news = ""

    if "ビジネス" in words:
        payload['category'] = "business"
        news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()
        news_dict = news_json['articles']
        for i in range(3):
            news += news_dict[i]['title']
            news += " "

    elif "エンタメ" in words or "芸能" in words:
        payload['category'] = "entertainment"
        news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()
        news_dict = news_json['articles']
        for i in range(3):
            news += news_dict[i]['title']
            news += " "

    elif "健康" in words or "ヘルス" in words:
        payload['category'] = "health"
        news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()
        news_dict = news_json['articles']
        for i in range(3):
            news += news_dict[i]['title']
            news += " "

    elif "科学" in words or "サイエンス" in words:
        payload['category'] = "science"
        news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()
        news_dict = news_json['articles']
        for i in range(3):
            news += news_dict[i]['title']
            news += " "

    elif "スポーツ" in words:
        payload['category'] = "sports"
        news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()
        news_dict = news_json['articles']
        for i in range(3):
            news += news_dict[i]['title']
            news += " "

    elif "IT" in words or "テクノロジー" in words:
        payload['category'] = "technology"
        news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()
        news_dict = news_json['articles']
        for i in range(3):
            news += news_dict[i]['title']
            news += " "

    else:
        news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()
        news_dict = news_json['articles']
        for i in range(3):
            news += news_dict[i]['title']
            news += " "

    return news
