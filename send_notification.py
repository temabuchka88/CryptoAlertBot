from aiogram import Bot, Router
from get_current_course import get_coin_price

router = Router()

async def notification(user, coin, upper_threshold, lower_threshold, bot: Bot):
    try:
        prise = get_coin_price(coin)
        upper_threshold = float(upper_threshold)
        lower_threshold = float(lower_threshold)

        if prise >= upper_threshold:
            await bot.send_message(chat_id=user, text=f'{coin} достиг вашего наивысшего предела в {prise} USD')

        elif prise <= lower_threshold:
            await bot.send_message(chat_id=user, text=f'{coin} достиг вашего низшего предела в {prise} USD')

    except Exception as e:
        print('Произошла ошибка:', e)