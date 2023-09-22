import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28645948"))
    API_HASH = os.environ.get("API_HASH", "0d1cca3a9f4f4beb7ae8508f05ec4fcd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6401922975:AAG1teIZxbqn-D0sokJjLDVvkL8uOlj-9_o")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKIBuwJIMK-prg3QrtJSB1J6zt5PVzrc7GiWyiYHY_eIf93aN0dVfyfb7ta8YHi_on4oowUy8j9eB7-Gctaz9qZdoBfQ5PLkRaurXRb24-e62it1lrctMUlZ9KNjXyKnV4rD8yMYVtBklkhLY-jjQf2VNySgrS2Mhnlyhb49z-OzJMBuI3YxC23VaWxLFBPm65RH9oXl21e2Ea12wgJ6woDYXsXT6N82hnA2EYbVj3CJJSF1WJmGaZAmmXHIhw_-fcZk-vsXEdhBCYJuEz1z4m_LXzE1oWG425HrExwPsiGQykM0y7OCMPdUmB3aAtzApevgWCvkrJ4rth2ZwPp7MBPgt-0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "music_princess_bot")
    SUPPORT = os.environ.get("SUPPORT", "the_rebel_princess_hindi_dubbed") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "the_rebel_princess_hindi_dubbed") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/87dde865db76f52e0df8b.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/bba41f45aeb36febb2ad9.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6610228180")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
