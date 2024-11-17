import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27857521"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "627b314d25c83e2c9a1a99db9ae0a3ef")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://naikmithun274:MPOo2wpAjCx49bEY@telegram.pdb2s.mongodb.net/?retryWrites=true&w=majority&appName=Telegram")
