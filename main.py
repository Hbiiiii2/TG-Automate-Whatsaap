import pandas as pd
import pywhatkit as kit
import time
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("log/bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Your token from BotFather
TOKEN = '7186757919:AAFJ1lzyHcaRl9jvw0AWMm_rr5YkxGI6y74'

# Define a function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('🤖 Halo! Saya adalah Bot Anda yang siap membantu! 🚀')
    update.message.reply_text(
        'Kirimkan file CSV dengan format "messages.csv". 📂\n\n'
        'Sebagai referensi, berikut contoh isi CSV-nya:'
    )
    update.message.reply_photo(photo=open('image.png', 'rb'))
    update.message.reply_text(
        '💡 Jangan khawatir, isi pesannya tidak harus persis sama seperti contoh.\n'
        '📋 Variasi dalam pesan juga bisa diterima!\n'
        'Selamat mencoba dan semoga sukses! 💪'
    )
    logger.info('Bot started and waiting for CSV file.')


# Define a function to handle CSV file upload
def handle_file(update: Update, context: CallbackContext) -> None:
    # Get the file
    file = update.message.document.get_file()
    file.download('messages.csv')
    logger.info('Received CSV file from user.')

    # Read the CSV file
    data = pd.read_csv('messages.csv', dtype={'phone_number': str})

    # Iterate through each row in the CSV and send messages
    for index, row in data.iterrows():
        name = row['name']
        phone_number = row['phone_number']
        message = row['message']

        # Send WhatsApp message
        try:
            kit.sendwhatmsg_instantly(f"+62{phone_number}", message)
            logger.info(f"Pesan terkirim kepada ({name}) +62{phone_number}")
            update.message.reply_text(f"✅ Pesan berhasil terkirim ke {name} (+62{phone_number})! 🎉")
            # Wait a few seconds before sending the next message
            time.sleep(15)
        except Exception as e:
            logger.error(f"Gagal mengirim pesan ke +62{phone_number}: {e}")
            update.message.reply_text(f"⚠️ Oops! Gagal mengirim pesan ke +62{phone_number}. 😢 Silakan coba lagi.")

def main():
    # Set up the Updater
    updater = Updater(TOKEN)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the file handler
    dispatcher.add_handler(MessageHandler(Filters.document.mime_type("text/csv"), handle_file))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
