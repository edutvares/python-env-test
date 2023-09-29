import os
from dotenv import load_dotenv
import string

load_dotenv()

BOT_API = os.getenv('BOT_API')
SITE_BANCA = os.getenv('SITE_BANCA')

with open('template.txt', 'r') as template_file:
    template = template_file.read()

template_obj = string.Template(template)

substituicoes = {'BOT_API': BOT_API, 'SITE_BANCA': SITE_BANCA}

resultado = template_obj.substitute(substituicoes)

print("----------------------------------------------")
print(resultado)
print("----------------------------------------------")