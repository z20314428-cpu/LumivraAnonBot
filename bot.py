from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from database import init_db, add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
    )

    await update.message.reply_text(
        f"""👋 سلام {user.first_name}

به LumivraAnonBot خوش اومدی.

بات با موفقیت راه‌اندازی شد.

🚀 نسخه حرفه‌ای در حال تکمیل است..."""
    )


def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
