from time import strftime
from xml.etree.ElementTree import tostring

import requests
import requests_cache
from config import *
import pandas as pd
from io import StringIO
import datetime
from twilio.rest import Client
import re


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

session = requests_cache.CachedSession(
    "api_cache",
    expire_after=3600
)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
alpha_vantage_endpoint_url = 'https://www.alphavantage.co/query'

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': alphavantage_api_key,
    'datatype': 'csv'
}

r = session.get(alpha_vantage_endpoint_url, params=stock_params)
r.raise_for_status()
stock_data = pd.read_csv(StringIO(r.text))
print(stock_data)

stock_price_percent_delta =  (stock_data["close"][0]/stock_data["close"][13] - 1 )*100
print(stock_price_percent_delta)

stock_price_percent_delta_format = ""
if stock_price_percent_delta > 0:
    stock_price_percent_delta_format = f"🔺{abs(stock_price_percent_delta):.0f}%"
elif stock_price_percent_delta < 0:
    stock_price_percent_delta_format = f"🔻{abs(stock_price_percent_delta):.0f}%"

if abs(stock_price_percent_delta) >= 5:

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    NEWS_API_ENDPOINT =  "https://newsapi.org/v2/everything"

    end_date =  datetime.date.today().strftime('%Y-%m-%d')
    start_date = (datetime.date.today() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')

    news_params = {
        'q': "("+ COMPANY_NAME + " OR " + STOCK + ")",
        'apiKey': news_api_key,
        'language': 'en',
        'searchIn': 'title,description',
        'from': start_date,
        'to': end_date,
        'pageSize': 3,
        'page': 1,
        'sortBy': 'publishedAt'          # relevance, popularity, publishedAt
    }

    news_response = session.get(NEWS_API_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    print(news_data)

    sms_list = [
        f"""{STOCK}: {stock_price_percent_delta_format}
    Headline: {item['title']}
    Brief: {re.split(r'[.\n]', item['description'])[0]}.
    """
        for item in news_data["articles"]
    ]
    for i in range(len(sms_list)):
        print(sms_list[i])

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     body="It might rain today, remember to bring an ☂️.",
    #     from_="+12164809245",
    #     to="+919815489141",
    # )
    #
    # print(message.status)

    for i in range(len(sms_list)):
        message = client.messages.create(
            body= sms_list[i],
            from_='whatsapp:+14155238886',
            to='whatsapp:+919815489141'
        )

        print(message.sid)



    #Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

