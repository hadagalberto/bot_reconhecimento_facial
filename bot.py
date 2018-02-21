import main
import time
import telepot
import chaves
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, "Me envie uma imagem")
    elif content_type == 'photo':
        bot.download_file(msg['photo'][-1]['file_id'], "images/" + msg['photo'][-1]['file_id'] + ".png")
        return_image = main.request_image(msg['photo'][-1]['file_id'] + ".png")
        foto = open(return_image, 'rb')
        #print(return_image)
        bot.sendPhoto(chat_id, foto)
        #print("enviado uma imagem")

TOKEN = chaves.bot_token

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Rodando ...')

while 1:
    time.sleep(10)
