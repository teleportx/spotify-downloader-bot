import os
from os import environ

from dotenv import load_dotenv

load_dotenv()

if not os.path.exists('data'):
    os.mkdir('data')


class Telegram:
    token = environ.get('TOKEN')


spotify_host = 'open.spotify.com'
temp_dir = 'songs'
