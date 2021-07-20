from YuiHirasawaMusicBot.config import config
from YuiHirasawaMusicBot.database import Database

db = Database(config.MONGODB_URI, config.DATABASE_NAME)
