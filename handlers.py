from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from .keyboard import create_keyboard
from .logic import process_search

class Form(StatesGroup):
    search_query = State()
    filters = State()

async def start(message: types.Message):
    await message.answer("Welcome! Use /search to find poems or /menu for options.")

async def search_command(message: types.Message):
    await Form.search_query.set()
    await message.answer("Enter a word or phrase to search:")

async def process_search_query(message: types.Message, state: FSMContext):
    query = message.text
    results = await process_search(query)
    
    if results:
        for result in results:
            preview = f"{result['first_line']}\n{result['context']}"
            await message.answer(preview, reply_markup=create_keyboard(result))
    else:
        await message.answer("No poems found. Try another search!")
    
    await state.finish()
