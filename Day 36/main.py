import requests
import os
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = ""
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

data = response.json()['Time Series (Daily)']

data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

price_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
    

print(price_difference)

diff_percentage = round((float(price_difference)/float(yesterday_closing_price)) * 100)
print(diff_percentage)


if abs(diff_percentage) > 2:
    news_parameters = {
        'qInTitle' : COMPANY_NAME,
        'apikey': NEWS_API_KEY, 
    }

    new_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    new_response.raise_for_status()
    news_articles = new_response.json()['articles']
    three_articles = news_articles[:3]
    message_body = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadlines: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
    print(message_body)


    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) 
    for article in message_body: 
        message = client.messages \
                        .create(
                            body=article,
                            from_='',
                            to=''
                        )

    print(message.status)