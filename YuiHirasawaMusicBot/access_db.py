from YuiHirasawaMusicBot import Config
from YuiHirasawaMusicBot.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
