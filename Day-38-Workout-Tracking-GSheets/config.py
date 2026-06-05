from dotenv import load_dotenv
import os

load_dotenv()

app_id = os.environ["APP_ID"]
app_key = os.environ["APP_KEY"]
gsheet_bearer_token = os.environ["GSHEET_BEARER_TOKEN"]
gsheet_endpoint = os.environ["GSHEET_ENDPOINT"]
