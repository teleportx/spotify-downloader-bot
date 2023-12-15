from aiogram import Router

from . import downloader

router = Router()

router.include_router(downloader.router)
