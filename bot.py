۱from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

from config import BOT_TOKEN, ADMIN_ID
from database import add_user, get_user_by_code, get_user_code, is_blocked
from utils import generate_code

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

waiting_reply = {}


@dp.message(CommandStart())
async def start(message: Message):
    user = message.from_user.id

    if is_blocked(user):
        await message.answer("❌ شما مسدود شده‌اید.")
        return

    data = get_user_code(user)

    if data is None:
        code = generate_code()
        add_user(user, code)
    else:
        code = data[0]

    link = f"https://t.me/{(await bot.get_me()).username}?start={code}"

    await message.answer(
        f"""سلام 🌹

لینک ناشناس اختصاصی شما:

{link}

این لینک را در کانال یا بیو قرار بده تا دیگران ناشناس برایت پیام بفرستند."""
    )


@dp.message(F.text.startswith("/start "))
async def anonymous(message: Message):
    sender = message.from_user.id

    if is_blocked(sender):
        return

    code = message.text.split()[1]

    user = get_user_by_code(code)

    if not user:
        await message.answer("لینک معتبر نیست.")
        return

    waiting_reply[sender] = user[0]

    await message.answer(
        "پیام خود را ارسال کنید."
    )
  
