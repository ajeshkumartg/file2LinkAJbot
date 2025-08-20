<p align="center">
<img src="https://www.vectorlogo.zone/logos/telegram/telegram-ar21.svg" alt="Telegram Logo" width="200"/>
</p>

<h1 align="center">Telegram File to Link Bot</h1>

<p align="center">
A powerful, self-hosted Telegram bot that converts files into direct downloadable links.
<br />
<br />
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version">
<img src="https://img.shields.io/badge/framework-Pyrogram-orange.svg" alt="Framework">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</p>

A powerful, self-hosted Telegram bot that converts files sent to it into direct downloadable links. Built with Pyrogram and designed to run on a Linux server, this bot can handle large files (up to 2GB) and includes features like automatic file cleanup and download progress indicators.

# 🌟 Features

- Large File Support: Bypasses Telegram's 20MB bot limit, supporting downloads up to 2GB.

- Direct Links: Generates direct HTTP links for easy sharing and downloading.

- Multi-File Handling: Supports documents, videos, photos, and audio files.

- Download Progress: Shows a real-time progress bar when downloading files.

- Duplicate File Check: Avoids re-downloading by providing a link to an existing file if a duplicate is sent.

- Automatic Cleanup: Automatically deletes files from the server after a configurable amount of time (default is 6 hours) to save space.

- Personalized & Supportive: Greets users by name and includes a "Buy Me a Coffee" link in all replies to support the developer.

- Organized Codebase: The project is structured into multiple files for easy maintenance and readability.


# 🏗️ Project Structure
The bot's code is organized into several files to keep it clean and manageable:

.
├── main.py             # The main entry point to run the bot.
├── config.py           # All your credentials and settings.
├── handlers.py         # The functions that handle user messages and commands.
├── utils.py            # Helper functions and background tasks (e.g., file cleanup).
└── requirements.txt    # A list of all necessary Python packages.

# 📋 Prerequisites

**Before you begin, you will need the following:**

- A Telegram Account: To get the necessary API credentials.

- A Telegram Bot Token: Obtained from @BotFather on Telegram.

- A Linux Server: A cloud VM (like Oracle Cloud's "Always Free" tier running Ubuntu) is perfect.

- Nginx Web Server: To serve the downloaded files.

- Python 3.8+ installed on your server.

# 🚀 Setup & Deployment
Follow these steps to get your bot up and running on an Ubuntu server.

1. Clone the Repository
Clone this repository into a directory of your choice on your server.

```
git clone https://github.com/ajeshkumartg/file2LinkAJbot.git
cd file2LinkAJbot
```

2. Install Dependencies
Install the required Python packages using the requirements.txt file.

```pip3 install -r requirements.txt```

3. Configure the Bot
This is the most important step. You need to provide your credentials and server details.

Rename the config.py.example to config.py (if you provide an example file).

Open config.py with a text editor (nano config.py).

Fill in all the required variables as explained in the Configuration Variables section below.

4. Set Up Nginx & Permissions
Your bot needs a web server to make the files accessible and a directory with the correct permissions to save them.

# Install Nginx
```sudo apt update && sudo apt install nginx -y```

# Create the download directory
```sudo mkdir -p /var/www/html/downloads```

# Set permissions (replace 'user' with your actual username)
```
sudo chown -R user:user /var/www/html/downloads
sudo chmod 755 /var/www/html/downloads
```

5. Run the Bot as a Service (Recommended)
To ensure your bot runs 24/7, set it up as a systemd service.

Create a new service file:

```sudo nano /etc/systemd/system/telegrambot.service```

Paste the following configuration into the file. Remember to replace user with your username and verify the paths.
```
[Unit]
Description=Pyrogram Telegram File Link Bot
After=network.target

[Service]
User=user
Group=user
WorkingDirectory=/home/user/file2LinkAJbot
ExecStart=/usr/bin/python3 /home/user/file2LinkAJbot/main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
Enable and start the service:
```
sudo systemctl daemon-reload
sudo systemctl enable telegrambot.service
sudo systemctl start telegrambot.service
```
Check the status to ensure it's running:

```sudo systemctl status telegrambot.service```

⚙️ Configuration Variables
All configuration is done in the config.py file.

| Variable         | Description                                 | Example                                 |
|------------------|---------------------------------------------|-----------------------------------------|
| `API_ID`         | Telegram API ID from my.telegram.org         | `12345`                                 |
| `API_HASH`       | Telegram API Hash from my.telegram.org       | `abc123def456`                          |
| `BOT_TOKEN`      | Bot token from @BotFather                   | `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`  |
| `SERVER_IP`      | The public IP address of your server. Do not include http://.| `141.123.45.67`                    |
| `DOWNLOAD_DIR`       | The absolute path on your server where files will be downloaded. Default is /var/www/html/downloads/.   | `/var/www/html/downloads`                     |
| `FILE_LIFETIME_SECONDS` | The duration (in seconds) a file should be stored before being deleted. Default is 21600 (6 hours). | ``                          |
| `CLEANUP_INTERVAL_SECONDS`           | How often (in seconds) the cleanup task should run to check for old files. Default is 600 (10 minutes) | ``                  |


📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
Thanks to the Pyrogram team for creating an amazing framework.

Inspired by the need for a simple, self-hosted file-to-link solution.
