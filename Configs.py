# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "26953933"))
    API_HASH = os.environ.get("API_HASH", "4bc2a58e7308a9da35bae33f68691d74")
    TOKEN = os.environ.get("TOKEN", "6803669543:AAFNzstLnDW4Seq7t3M-ReK1tBu9POuv9xo")
