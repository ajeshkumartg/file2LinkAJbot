# main.py
import asyncio
import logging
from pyrogram import Client, idle, filters
from pyrogram.handlers import MessageHandler

import config
from utils import cleanup_files
from handlers import start_command, file_handler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

app = Client(
    "my_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

start_handler = MessageHandler(start_command, filters.command("start"))
app.add_handler(start_handler)

all_media_filter = (filters.document | filters.photo | filters.video | filters.audio)
files_handler = MessageHandler(file_handler, all_media_filter)
app.add_handler(files_handler)

async def main():
    """Starts the bot and the background cleanup task."""
    await app.start()
    log.info("Bot has started...")
    asyncio.create_task(cleanup_files())
    await idle()
    await app.stop()
    log.info("Bot has stopped.")

if __name__ == "__main__":
    app.run(main())