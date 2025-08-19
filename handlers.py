# handlers.py
import os
import logging
from urllib.parse import quote
from pyrogram.types import Message
import config
from utils import humanbytes

log = logging.getLogger(__name__)

async def start_command(client: "Client", message: Message):
    """Sends a personalized welcome message with a button."""
    await message.reply_text(
        f"Hi.. {message.from_user.first_name}!\n\n"
        "I can download files up to 2GB.\n"
        "Send me any file and I will generate a direct link for you.\n\n"
        "Files are automatically deleted after 6 hours.",
        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
    )

async def file_handler(client: "Client", message: Message):
    """Handles any received file, checks for duplicates, downloads it, and replies with a link."""
    file_object = message.document or message.video or message.audio or message.photo
    if not file_object:
        return

    original_filename = getattr(file_object, 'file_name', f"{file_object.file_unique_id}.{file_object.mime_type.split('/')[-1]}")
    file_path = os.path.join(config.DOWNLOAD_DIR, original_filename)

    if os.path.exists(file_path):
        log.info(f"Duplicate file found: {original_filename}. Sharing existing link.")
        file_size = os.path.getsize(file_path)
        formatted_size = humanbytes(file_size)
        encoded_filename = quote(original_filename)
        direct_link = f"http://{config.SERVER_IP}/downloads/{encoded_filename}"
        await message.reply_text(
            f"✅ **File already exists on server!**\n\n"
            f"📄 _File Name: {original_filename}_\n"
            f"💾 _Size: {formatted_size}_\n\n"
            f"🔗 **Direct Link:** {direct_link}\n\n"
            f"_(This file will be deleted in 6 hours)_",
            disable_web_page_preview=True,
            quote=True,
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )
        return

    status_message = await message.reply_text(
        "Preparing to download...", 
        quote=True,
        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
    )
    try:
        last_reported_percentage = -1
        async def progress(current, total):
            nonlocal last_reported_percentage
            percentage = int(current * 100 / total)
            if percentage > last_reported_percentage and (percentage % 5 == 0 or percentage == 100):
                try:
                    await status_message.edit_text(
                        f"Downloading... **{percentage}%**",
                        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
                    )
                    last_reported_percentage = percentage
                except Exception: pass

        await message.download(file_name=file_path, progress=progress)
        os.chmod(file_path, 0o644)
        file_size = os.path.getsize(file_path)
        formatted_size = humanbytes(file_size)
        encoded_filename = quote(original_filename)
        direct_link = f"http://{config.SERVER_IP}/downloads/{encoded_filename}"
        await status_message.edit_text(
            f"✅ **File downloaded successfully!**\n\n"
            f"📄 _File Name: {original_filename}_\n"
            f"💾 _Size: {formatted_size}_\n\n"
            f"🔗 **Direct Link:** {direct_link}\n\n"
            f"_(This file will be deleted in 6 hours)_",
            disable_web_page_preview=True,
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )
    except Exception as e:
        log.error(f"Error handling file: {e}")
        await status_message.edit_text(
            f"❌ **Sorry, an error occurred:**\n\n`{e}`",
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )# handlers.py
import os
import logging
from urllib.parse import quote
from pyrogram.types import Message
import config
from utils import humanbytes

log = logging.getLogger(__name__)

async def start_command(client: "Client", message: Message):
    """Sends a personalized welcome message with a button."""
    await message.reply_text(
        f"Hi.. {message.from_user.first_name}!\n\n"
        "I can download files up to 2GB.\n"
        "Send me any file and I will generate a direct link for you.\n\n"
        "Files are automatically deleted after 6 hours.",
        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
    )

async def file_handler(client: "Client", message: Message):
    """Handles any received file, checks for duplicates, downloads it, and replies with a link."""
    file_object = message.document or message.video or message.audio or message.photo
    if not file_object:
        return

    original_filename = getattr(file_object, 'file_name', f"{file_object.file_unique_id}.{file_object.mime_type.split('/')[-1]}")
    file_path = os.path.join(config.DOWNLOAD_DIR, original_filename)

    if os.path.exists(file_path):
        log.info(f"Duplicate file found: {original_filename}. Sharing existing link.")
        file_size = os.path.getsize(file_path)
        formatted_size = humanbytes(file_size)
        encoded_filename = quote(original_filename)
        direct_link = f"http://{config.SERVER_IP}/downloads/{encoded_filename}"
        await message.reply_text(
            f"✅ **File already exists on server!**\n\n"
            f"📄 _File Name: {original_filename}_\n"
            f"💾 _Size: {formatted_size}_\n\n"
            f"🔗 **Direct Link:** {direct_link}\n\n"
            f"_(This file will be deleted in 6 hours)_",
            disable_web_page_preview=True,
            quote=True,
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )
        return

    status_message = await message.reply_text(
        "Preparing to download...", 
        quote=True,
        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
    )
    try:
        last_reported_percentage = -1
        async def progress(current, total):
            nonlocal last_reported_percentage
            percentage = int(current * 100 / total)
            if percentage > last_reported_percentage and (percentage % 5 == 0 or percentage == 100):
                try:
                    await status_message.edit_text(
                        f"Downloading... **{percentage}%**",
                        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
                    )
                    last_reported_percentage = percentage
                except Exception: pass

        await message.download(file_name=file_path, progress=progress)
        os.chmod(file_path, 0o644)
        file_size = os.path.getsize(file_path)
        formatted_size = humanbytes(file_size)
        encoded_filename = quote(original_filename)
        direct_link = f"http://{config.SERVER_IP}/downloads/{encoded_filename}"
        await status_message.edit_text(
            f"✅ **File downloaded successfully!**\n\n"
            f"📄 _File Name: {original_filename}_\n"
            f"💾 _Size: {formatted_size}_\n\n"
            f"🔗 **Direct Link:** {direct_link}\n\n"
            f"_(This file will be deleted in 6 hours)_",
            disable_web_page_preview=True,
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )
    except Exception as e:
        log.error(f"Error handling file: {e}")
        await status_message.edit_text(
            f"❌ **Sorry, an error occurred:**\n\n`{e}`",
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )# handlers.py
import os
import logging
from urllib.parse import quote
from pyrogram.types import Message
import config
from utils import humanbytes

log = logging.getLogger(__name__)

async def start_command(client: "Client", message: Message):
    """Sends a personalized welcome message with a button."""
    await message.reply_text(
        f"Hi.. {message.from_user.first_name}!\n\n"
        "I can download files up to 2GB.\n"
        "Send me any file and I will generate a direct link for you.\n\n"
        "Files are automatically deleted after 6 hours.",
        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
    )

async def file_handler(client: "Client", message: Message):
    """Handles any received file, checks for duplicates, downloads it, and replies with a link."""
    file_object = message.document or message.video or message.audio or message.photo
    if not file_object:
        return

    original_filename = getattr(file_object, 'file_name', f"{file_object.file_unique_id}.{file_object.mime_type.split('/')[-1]}")
    file_path = os.path.join(config.DOWNLOAD_DIR, original_filename)

    if os.path.exists(file_path):
        log.info(f"Duplicate file found: {original_filename}. Sharing existing link.")
        file_size = os.path.getsize(file_path)
        formatted_size = humanbytes(file_size)
        encoded_filename = quote(original_filename)
        direct_link = f"http://{config.SERVER_IP}/downloads/{encoded_filename}"
        await message.reply_text(
            f"✅ **File already exists on server!**\n\n"
            f"📄 _File Name: {original_filename}_\n"
            f"💾 _Size: {formatted_size}_\n\n"
            f"🔗 **Direct Link:** {direct_link}\n\n"
            f"_(This file will be deleted in 6 hours)_",
            disable_web_page_preview=True,
            quote=True,
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )
        return

    status_message = await message.reply_text(
        "Preparing to download...", 
        quote=True,
        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
    )
    try:
        last_reported_percentage = -1
        async def progress(current, total):
            nonlocal last_reported_percentage
            percentage = int(current * 100 / total)
            if percentage > last_reported_percentage and (percentage % 5 == 0 or percentage == 100):
                try:
                    await status_message.edit_text(
                        f"Downloading... **{percentage}%**",
                        reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
                    )
                    last_reported_percentage = percentage
                except Exception: pass

        await message.download(file_name=file_path, progress=progress)
        os.chmod(file_path, 0o644)
        file_size = os.path.getsize(file_path)
        formatted_size = humanbytes(file_size)
        encoded_filename = quote(original_filename)
        direct_link = f"http://{config.SERVER_IP}/downloads/{encoded_filename}"
        await status_message.edit_text(
            f"✅ **File downloaded successfully!**\n\n"
            f"📄 _File Name: {original_filename}_\n"
            f"💾 _Size: {formatted_size}_\n\n"
            f"🔗 **Direct Link:** {direct_link}\n\n"
            f"_(This file will be deleted in 6 hours)_",
            disable_web_page_preview=True,
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )
    except Exception as e:
        log.error(f"Error handling file: {e}")
        await status_message.edit_text(
            f"❌ **Sorry, an error occurred:**\n\n`{e}`",
            reply_markup=config.BUY_ME_A_COFFEE_KEYBOARD
        )