from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.environ.get("SECRET_KEY")
URL = os.environ.get("MONGO_URL")
SSN = os.environ.get("SESSION_KEY")