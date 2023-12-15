import string
from os import environ

from dotenv import load_dotenv

load_dotenv()


class Telegram:
    token = environ.get('TOKEN')


spotify_host = 'open.spotify.com'
temp_dir = 'songs'
