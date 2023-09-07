import logging

from aiogram import Bot, Dispatcher, executor, types

import inline_keyboard
import messages
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'weather'])
async def show_weather(message: types.Message):
    await message.answer(text=await messages.weather(),
                         reply_markup=inline_keyboard.WEATHER)


@dp.message_handler(commands='help')
async def show_help_message(message: types.Message):
    await message.answer(text=f'This bot can get the current weather from your IP address.',
                         reply_markup=inline_keyboard.HELP)


@dp.message_handler(commands='wind')
async def show_wind(message: types.Message):
    await message.answer(text=await messages.wind(), reply_markup=inline_keyboard.WIND)


@dp.message_handler(commands='sun_time')
async def show_sun_time(message: types.Message):
    await message.answer(text=await messages.sun_time(), reply_markup=inline_keyboard.SUN_TIME)


@dp.callback_query_handler(text='weather')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await callback_query.answer(text=await messages.weather(),
                                show_alert=True,
                                cache_time=config.CACHE_TIME)


@dp.callback_query_handler(text='wind')
async def process_callback_wind(callback_query: types.CallbackQuery):
    await callback_query.answer(text=await messages.wind(),
                                show_alert=True,
                                cache_time=config.CACHE_TIME)


@dp.callback_query_handler(text='sun_time')
async def process_callback_sun_time(callback_query: types.CallbackQuery):
    await callback_query.answer(text=await messages.sun_time(),
                                show_alert=True,
                                cache_time=config.CACHE_TIME)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
