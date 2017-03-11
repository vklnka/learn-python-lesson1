#learn1_vklnka_bot  API 316677648:AAFjbNydhFfBZAgzEvx4u2Xvj_OpDsSENqk

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot, update): #две переменные всегда
    print('Вызван /start')
    print(update)
    bot.sendMessage(update.message.chat_id, text='Говори мяшок с мясом!') #sendMessage послать сообщение message.chat_id послать сообщение по айди которое у нас присылает телеграм что бы мы попали в точно тот чат

def show_error(bot, update, error):
    print(error)

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text)) #update.message.text - то что мы написали боту
    bot.sendMessage(update.message.chat_id, update.message.text)

def main():
    updater = Updater("316677648:AAFjbNydhFfBZAgzEvx4u2Xvj_OpDsSENqk")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) #add_handler добавить обработчик, CommandHandler тип обработчика
    dp.add_handler(MessageHandler([Filters.text], talk_to_me)) #Filters.text вызывает только когда придет текст
    dp.add_error_handler(show_error) # обработчик ошибок add_error_handler(show_error - имя функции которая вызывается когда что то пошло не так)
    updater.start_polling()
    updater.idle()

main()