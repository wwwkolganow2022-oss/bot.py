import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💰 Купить доступ", callback_data="buy")],
        [InlineKeyboardButton(text="📱 Поддержка", callback_data="support")]
    ])
    await message.answer("Привет! Это твой бот для заработка.", reply_markup=keyboard)

@dp.callback_query()
async def handle(call: types.CallbackQuery):
    await call.message.answer("Функция оплаты подключается через BotFather.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
