from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "20661683"
# -------------------------------------------------------------
API_HASH = "596794978e0a1b5cb03e76243de90e80"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "deepak-bot"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "8195333063"))
BOT_ID = int(getenv("BOT_ID", "7671407152"))
SUPPORT_GRP = "UFC_UPDATES"
UPDATE_CHNL = "ll_P_U_L_lI"
OWNER_USERNAME = "silenthrax"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002286471112"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "8195333063").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
 
# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/UFCUPDATES/INAYA_CHAT",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
