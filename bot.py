import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
from dotenv import load_dotenv
import handlers

load_dotenv()
telegram_token = os.getenv("BOT_TOKEN")
bot = Bot(telegram_token)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    scheduler = AsyncIOScheduler(temezone="Europe/Minsk")
    scheduler.start()
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(handlers.router)

    await dp.start_polling(bot, scheduler=scheduler)


if __name__ == "__main__":
    asyncio.run(main())