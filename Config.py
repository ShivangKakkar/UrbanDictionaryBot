import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    API_ID = int(os.environ.get('API_ID', 0))
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
