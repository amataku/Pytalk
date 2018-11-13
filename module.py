# coding:utf-8
import requests
import json
import os
from PIL import Image

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
            print(news_dict[i]['title'])
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
            print(news_dict[i]['title'])
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
            print(news_dict[i]['title'])
            news += news_dict[i]['title']
            news += " "

    return news

def return_weather(words):
    payload = {
        'city' : os.environ['CITY_ID']
    }
    weather = ""

    if "明日" in words:
        weather_json = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1', params = payload).json()
        weather += "明日の天気は、"
        weather += weather_json["forecasts"][1]["telop"]
        weather += "です。最高気温は、"
        weather += weather_json["forecasts"][1]["temperature"]["max"]["celsius"]
        weather += "度、最低気温は、"
        weather += weather_json["forecasts"][1]["temperature"]["min"]["celsius"]
        weather += "度です。"
    else:
        weather_json = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1', params = payload).json()
        weather += "今日の天気は、"
        weather += weather_json["forecasts"][0]["telop"]
        weather += "です。最高気温は、"
        weather += weather_json["forecasts"][0]["temperature"]["max"]["celsius"]
        weather += "度です。"

    return weather

def return_map(file_path):
    image = Image.open(file_path)
    image.show()
