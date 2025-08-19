# config.py
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- BOT CONFIGURATION ---
API_ID =   # Replace with your API ID
API_HASH = ""  # Replace with your API Hash
BOT_TOKEN = "" # Replace with your bot token

# --- SERVER CONFIGURATION ---
SERVER_IP = "" # Replace with your Oracle instance's Public IP
DOWNLOAD_DIR = "/var/www/html/downloads/"

# --- FILE CLEANUP CONFIGURATION ---
FILE_LIFETIME_SECONDS = 6 * 3600  # 6 hours
CLEANUP_INTERVAL_SECONDS = 600    # 10 minutes

# # --- REUSABLE MARKUP ---
BUY_ME_A_COFFEE_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Buy Me a Coffee ☕", url=""
            )
        ]
    ]
)
