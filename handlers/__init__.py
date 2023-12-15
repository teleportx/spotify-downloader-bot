from aiogram import Router

from . import start
from . import downloader

router = Router()

router.include_router(start.router)
router.include_router(downloader.router)
