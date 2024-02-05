import os
from telethon import TelegramClient
api_id = 20544260
api_hash = "a0b00461d3fba22aa186fa648d77787e"
bot_token = "6768420785:AAFqlFpxDVOS4M761pIAzrls_2pUK5jfOQQ"
skeleton_url = ""

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
skeleton_url = os.environ.get('SKELETON_URL')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


