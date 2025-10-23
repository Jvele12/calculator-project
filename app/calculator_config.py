from dotenv import load_dotenv
import os

load_dotenv()

# ---------- Directory Settings ----------
LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "history")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(HISTORY_DIR, exist_ok=True)

# ---------- File Settings ----------
HISTORY_FILE = os.path.join(HISTORY_DIR, "calculator_history.csv")
LOG_FILE = os.path.join(LOG_DIR, "calculator.log")

# ---------- History Settings ----------
AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))

# ---------- Calculation Settings ----------
PRECISION = int(os.getenv("CALCULATOR_PRECISION", "2"))
MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "100000"))
DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
