from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater=Updater(token='5208369126:AAG354DZTYxQ7FPotVY4VqTf_7CUNKJpjwA',use_context=True)
dispatcher=updater.dispatcher

updater.start_polling()

def hello(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="hello, world" )

hello_handler=CommandHandler('hello',hello)
dispatcher.add_handel(hello_handler)

