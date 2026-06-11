from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8878828937:AAE3ZWZtW58kER2QYYjva9znusjHkrESxaU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📏 Metric (kg/cm)", callback_data="metric")],
        [InlineKeyboardButton("📐 Imperial (lb/ft)", callback_data="imperial")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "⚖️ BMI Myanmar\n\nယူနစ်ရွေးပါ👇",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "metric":
        await query.edit_message_text(
            "📏 Metric Mode\n\n⚖️ ကိုယ်အလေးချိန် (kg) ထည့်ပါ။"
        )

    elif query.data == "imperial":
        await query.edit_message_text(
            "📐 Imperial Mode\n\n⚖️ Weight (lb) ထည့်ပါ။"
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("BMI Myanmar Running...")
app.run_polling()
