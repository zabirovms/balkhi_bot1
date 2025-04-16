from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import start, search_command
from config import BOT_TOKEN

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Register handlers
dp.register_message_handler(start, commands=["start"])
dp.register_message_handler(search_command, commands=["search"])

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
