import telebot
from tgbot import config
from photo_processing_service import PhotoProcessingService

bot = telebot.TeleBot(config.TOKEN, num_threads=5)


def send_welcome(message):
    bot.send_message(message.from_user.id, "Привет! Отправь фото, которое хочешь обработать.")

@bot.message_handler(content_types=['photo'])
def send_photo_step(message):
    try:
        received_photo = message.photo
        file_path = bot.get_file(received_photo[-1].file_id).file_path
        downloaded_file = bot.download_file(file_path)
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)

        msg = bot.reply_to(message, """\
        Теперь задай позиции переднего и заднего света 
        """)
        bot.register_next_step_handler(msg, set_params_step)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Похоже это не фото')

def set_params_step(message):
    params = message.text.split()
    bot.send_message(message.from_user.id, "Фото обрабатывается")
    res_photo = PhotoProcessingService().call("image.jpg", params)
    img = open(res_photo, 'rb')
    bot.send_photo(message.from_user.id, img)
    img.close()

def register_handlers():
    bot.register_message_handler(send_welcome, commands=['start'], admin=True, pass_bot=True)

register_handlers()

def run():
    bot.infinity_polling()

run()
