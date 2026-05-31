from groq import Groq
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = "8889653619:AAF8NCABlPQIvVCZRKLN6xT2rDep41V3VPo"
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Ты вежливый помощник. Отвечай кратко на языке собеседника."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=1000
    )
    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
