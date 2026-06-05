from dotenv import load_dotenv
import os

load_dotenv()

alphavantage_api_key = os.environ["ALPHA_VANTAGE_API_KEY"]
news_api_key = os.environ["NEWS_API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

