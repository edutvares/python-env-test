import os
from dotenv import load_dotenv

load_dotenv()

BOT_API = os.getenv('BOT_API')
SITE_BANCA = os.getenv('SITE_BANCA')

print("----------------------------------------------")
print("Key: ", BOT_API)
print("Site: ", SITE_BANCA)
print("----------------------------------------------")