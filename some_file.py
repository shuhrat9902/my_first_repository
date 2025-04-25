from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "7686271669:AAE_lJXmRYxU_R1Ql_zo6oRovJlvKVlOJCg"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



def pretty_json(obj):
    print(obj.model_dump_json(indent=4, exclude_none=True))


async def start_command(message: Message) -> None:
    await message.answer("Hello! I'm a bot. How can I assist you today?")


async def help_command(message: Message) -> None:
    await message.answer(
        "Here are some commands you can use:\n/start - Start the bot\n/help - Get help"
    )


@dp.message(F.text)
async def echo_message(message: Message) -> None:
    print("Вы прислали текстовое сообщение")
    await message.reply(text="Вы прислали текстовое сообщение")


@dp.message(F.photo)
async def echo_photo(message: Message) -> None:
    print("Вы прислали фото")
    await message.answer("Вы прислали фото")
    await message.reply_photo(photo=message.photo[0].file_id)


async def echo_video(message: Message) -> None:
    print("Вы прислали видео")
    await message.reply_video(video=message.video.file_id)


async def echo_gif(message: Message) -> None:
    print("Вы прислали гифку")
    await message.reply_animation(animation=message.animation.file_id)


async def echo_document(message: Message) -> None:
    print("Вы прислали документ")
    await message.reply_document(document=message.document.file_id)


async def echo_audio(message: Message) -> None:
    print("Вы прислали аудио")
    await message.reply_audio(audio=message.audio.file_id)


async def echo_voice(message: Message) -> None:
    print("Вы прислали голосовое сообщение")
    await message.reply_voice(voice=message.voice.file_id)


async def echo_sticker(message: Message) -> None:
    print("Вы прислали стикер")
    await message.answer(
        text="Какой прикольный стикер! Нужно еще раз его посмотреть) \n\n Вот он:"
    )
    await message.reply_sticker(sticker=message.sticker.file_id)


dp.message.register(start_command, Command(commands=["start"]))
dp.message.register(help_command, Command(commands=["help"]))
dp.message.register(echo_photo, F.photo)
dp.message.register(echo_video, F.video)
dp.message.register(echo_gif, F.animation)
dp.message.register(echo_document, F.document)
dp.message.register(echo_audio, F.audio)
dp.message.register(echo_voice, F.voice)
dp.message.register(echo_sticker, F.sticker)
dp.message.register(echo_message)


if __name__ == "__main__":
    dp.run_polling(bot, skip_updates=True)
