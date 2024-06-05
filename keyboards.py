from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def coins_keyborad():
    coins = [
        "BTC",
        "ETH",
        "BNB",
    ]
    buttons = []
    for coin in coins:
        button = InlineKeyboardButton(text=coin, callback_data=coin)
        buttons.append([button])
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb