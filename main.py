import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

telegram_token = "6027405487:AAHWI_lUyGvDxmAKuKPLfUuAT8ZJ4fOHFaQ"
openai.api_key = "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"

bot = Bot(telegram_token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

    await message.answer(response['choices'][0]['text'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
