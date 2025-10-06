from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Configuration variables
HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")
AUTOSAVE = os.getenv("AUTOSAVE", "True").lower() == "true"

