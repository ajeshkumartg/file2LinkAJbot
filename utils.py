
import os
import time
import asyncio
import logging
import config

log = logging.getLogger(__name__)

def humanbytes(B):
    """Return the given bytes as a human-friendly string."""
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)
    GB = float(KB ** 3)
    TB = float(KB ** 4)

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B/KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B/MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B/GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B/TB)

async def cleanup_files():
    """Periodically checks for and deletes old files."""
    log.info("Cleanup task started.")
    while True:
        try:
            for filename in os.listdir(config.DOWNLOAD_DIR):
                file_path = os.path.join(config.DOWNLOAD_DIR, filename)
                if os.path.isfile(file_path):
                    file_age = time.time() - os.path.getmtime(file_path)
                    if file_age > config.FILE_LIFETIME_SECONDS:
                        os.remove(file_path)
                        log.info(f"Deleted old file: {filename}")
        except Exception as e:
            log.error(f"Error during cleanup: {e}")
        
        await asyncio.sleep(config.CLEANUP_INTERVAL_SECONDS)