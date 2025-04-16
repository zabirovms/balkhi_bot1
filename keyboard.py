from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_keyboard(poem):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("View Full Poem", callback_data=f"full_poem:{poem['poem_id']}"),
        InlineKeyboardButton("New Search", callback_data="new_search"),
        InlineKeyboardButton("Main Menu", callback_data="main_menu")
    )
    return keyboard
