import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID", "")
GOOGLE_SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "ericklie95")

WEATHER_LAT = float(os.getenv("WEATHER_LAT", "-33.8688"))
WEATHER_LON = float(os.getenv("WEATHER_LON", "151.2093"))
