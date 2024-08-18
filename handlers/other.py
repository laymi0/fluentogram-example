from aiogram import Router
from aiogram.types import Message
from fluentogram import TranslatorRunner

other_router = Router()


@other_router.message()
async def send_echo(message: Message, i18n: TranslatorRunner):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=i18n.no.copy())