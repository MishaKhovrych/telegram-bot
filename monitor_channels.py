from pyrogram import Client
import requests

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_WEBHOOK_URL = "http://localhost:8000/process_content"
REFERENCE_CHANNELS = ["@trade001k", "@online_insider"]

app = Client("monitor_session", api_id=API_ID, api_hash=API_HASH)

@app.on_message()
def monitor_channels(client, message):
    if message.chat.username in REFERENCE_CHANNELS:
        content = {
            "channel": message.chat.username,
            "text": message.text,
            "date": message.date
        }
        response = requests.post(BOT_WEBHOOK_URL, json=content)
        if response.status_code == 200:
            print(f"Контент из {message.chat.username} успешно обработан ботом.")

app.run()