# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "3939406"))
    API_HASH = os.environ.get("API_HASH", "e11d0eaec136b1047974ab098041e9f2")
    TOKEN = os.environ.get("TOKEN", "6904551522:AAH9TXT-72JQgsiUpdo-uXggXLASpZL4Y0o")
