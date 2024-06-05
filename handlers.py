from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import coins_keyborad
from states import CoinStep
from send_notification import notification
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
router = Router()

@router.message(Command("start"))
async def choose_coins(message: Message, state: FSMContext):
    await message.answer("Выберите криптовалюту для отслеживания курса:",reply_markup=coins_keyborad())
    await state.update_data(user=message.from_user.id)
    await state.set_state(CoinStep.upper_threshold)

@router.callback_query(CoinStep.upper_threshold)
async def select_upper_threshold(callback: CallbackQuery, state: FSMContext):
    await state.update_data(coin=callback.data)
    await callback.message.edit_text("Введите верхний предел:")
    await state.set_state(CoinStep.lower_threshold)

@router.message(CoinStep.lower_threshold)
async def select_lower_threshold(message: Message, state: FSMContext):
    await state.update_data(upper_threshold=message.text)
    await message.answer("Введите нижний предел:")
    await state.set_state(CoinStep.accept)

@router.message(CoinStep.accept)
async def accept(message: Message, state: FSMContext, scheduler: AsyncIOScheduler, bot: Bot):
    await state.update_data(lower_threshold=message.text)
    data = await state.get_data()
    user = data.get('user')
    coin = data.get('coin')
    upper_threshold = data.get('upper_threshold')
    lower_threshold = data.get('lower_threshold')
    await message.answer(f"Вам будет отправлено уведомление, когда {coin} достигнет {upper_threshold} USD по верхнему пределу или {lower_threshold} UDS по нижнему пределу.")

    scheduler.add_job(
    notification,
    trigger=IntervalTrigger(minutes=1),
    kwargs={'user': user, 'coin': coin, 'upper_threshold': upper_threshold, 'lower_threshold': lower_threshold, 'bot': bot}
)

    await state.clear()