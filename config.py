import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "14050586")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Animes_India_bot') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Turn this feature on or off using True or False put value inside  ""
    # TRUE for yes FALSE if no 
    TOKEN = True if os.environ.get('TOKEN', "True") == "True" else False 
    SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "")
    SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
    VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
    IS_VERIFY = os.environ.get("IS_VERIFY", "True")
    TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "5446367898")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002317509038')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/219c7ce28f8f9262c3477-5ac482fb1d0adadca5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
🚀 **File Successfully Processed!** 🌟  

📂 **File Name:** `{0}` 📝✨  
📏 **Original Size:** `{1}` 📦📏  
🗜 **Encoded Size:** `{2}` 🔐💾  
📉 **Compression:** `{3}%` 📊🔽  

⏬ **Downloaded in:** `{4}` ⏳📥  
⚙️ **Encoded in:** `{5}` ⚡🎛  
☁️ **Uploaded in:** `{6}` 🚀📤  

🔥 **Your file is compressed, optimized, and ready to go!** 😎✨
"""
