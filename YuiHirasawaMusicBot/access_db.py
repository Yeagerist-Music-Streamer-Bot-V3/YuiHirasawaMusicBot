from YuiHirasawaMusicBot import config
from YuiHirasawaMusicBot.database import Database

db = Database(config.MONGODB_URI, config.SESSION_NAME)
