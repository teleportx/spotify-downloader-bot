import asyncio
import json
import logging
import os
import re
import shutil

from aiogram import Router
from aiogram import types
from aiogram.types import FSInputFile

import config

router = Router()


if not os.path.exists(config.temp_dir):
    os.mkdir(config.temp_dir)

else:
    for file in os.listdir(config.temp_dir):
        shutil.rmtree(f'{config.temp_dir}/{file}')

with open('users.json', 'a+') as fp:
    fp.seek(0)
    if fp.read() == '':
        fp.write('[]')
        users = []

    else:
        try:
            fp.seek(0)
            users = json.load(fp)

        except json.JSONDecodeError:
            raise IOError('Failed to parse users.json')


urlregex = re.compile(rf'^https://{config.spotify_host}(/?|[/?]\S+)$', re.IGNORECASE)


@router.message()
async def download_song(message: types.Message):
    if message.chat.id not in users:
        logging.warning(f'User {message.chat.id} trying to get access')
        return

    url = message.text
    valid = re.match(urlregex, url) is not None

    if not valid:
        await message.reply('You sent bad link!')
        return

    answer = await message.reply('Starting download...')

    path = f'{config.temp_dir}/{message.message_id}/{url[32:url.find("?")]}'
    executing = await asyncio.create_subprocess_shell(f'spotifydl --o {path} --oo {url}',
                                                      stderr=asyncio.subprocess.DEVNULL)  # The creator of spotifydl writes all logs to stderr
    await executing.communicate()

    path += '/'
    song_file = FSInputFile(path + sorted(os.listdir(path))[1])
    await message.reply_audio(song_file)

    await answer.delete()
    shutil.rmtree(f'{config.temp_dir}/{message.message_id}')
