from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5668579633:AAFC9xadqj2GITH1ef6zFTaTAwi1UXO--qA",
                                    use_context=True)
# ? Start the bot
def start(update: Update, context: CallbackContext):
        update.message.reply_text(
                    "Hello sir, Welcome to the Bot.Please write\
                    /help to see the commands available.")

def help(update: Update, context: CallbackContext):
        update.message.reply_text("""Available Commands :-
        /TODO - TODO TEXT
        """)


def showTodo(update: Update, context: CallbackContext):
        update.message.reply_text(
                    "Please add a TODO")


# ? Filter Function
def unknown(update: Update, context: CallbackContext):
        update.message.reply_text(
                    "Sorry '%s' is not a valid command" % update.message.text)

# ? Filter Function
def unknown_text(update: Update, context: CallbackContext):
        update.message.reply_text(
                    "Sorry I can't recognize you , you said '%s'" % update.message.text)

def main():
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('show', showTodo))


    # * Filter for unknown commands
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.command, unknown))  # Filters out unknown commands

    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    updater.start_polling()


if __name__ == "__main__":
    main()