import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27857521"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "627b314d25c83e2c9a1a99db9ae0a3ef")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7024087501"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://manassahu9044889:EY7DrKItRIAZ2Fdb@cluster0.rnugd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
