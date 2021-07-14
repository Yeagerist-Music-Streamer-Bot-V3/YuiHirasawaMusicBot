from config import Config
from .database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
