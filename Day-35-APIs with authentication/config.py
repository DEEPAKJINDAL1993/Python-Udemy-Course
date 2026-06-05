from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
ow_api_key = os.environ["OW_API_KEY"]

