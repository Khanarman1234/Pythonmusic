import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28645948"))
    API_HASH = os.environ.get("API_HASH", "0d1cca3a9f4f4beb7ae8508f05ec4fcd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6494645239:AAFMt0zq7GQbpx7QQetXv04DNq9cPG3FDzU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBu6n4Xavu9UzGPfnzrpZcxwNxIPcOFJ6Yjo5shY-rcVoSnJHVGNNNxxOY7fXMrZ3Vv5xEUYuxd1O5Q_mQhdAmZiMVa7pSSKK6AnWbVmEAXrtiHnQsHvu0z82UnL2YNFSIlZ68I8WdEZBM3-YOD4J0x63sDamYQE2mYjJLJOl8zWnXTJUEzDovT0ct9LimJqgQJr6JDuVAfVY1ajzYg9Wiz-cs-1d5H5tW7ykaErF3XIsbPZ1SG1nQJjEvtuiRQ9Z1tA8Sp48LVhcHEzp50RIApUHAIy9DySyQoFbXKbszvLDgaH3H6kBdkxg_coaVUKuqoG9F5RwTziiBZsWkbMoVoXY=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mr_hayato_robot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/log_group1") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/log_group1") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/429f48afd7391269a550e.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/35184d0ec3f4befa51dbc.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6412641300")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
