import os

from Bot.TeleBot import TeleBot
from Bot.Model.Message import Message, ParseMode
from Bot.Model.Update import Update

API_KEY = os.getenv('telegramApiKey')
bot = TeleBot(API_KEY)


# Just listening to updated
def update(update: Update):
    bot.send_message(message.chat.getID(), "<b>Hello</b>", parse_mode=ParseMode.HTML.value)


# Forwarding message in telegram bot
@bot.add_regex_helper(regex=["^forward message$", "^fwd message$"])
def send_bold(message: Message):
    print(bot.forward_messaged(chat_id=message.chat.getID(), from_chat_id=message.chat.getID(),
                               message_id=message.get_id()))


# Getting information about the bot
@bot.add_regex_helper(regex="^get me$")
def send_bold(message: Message):
    info = bot.get_me()
    bot.send_message(message.chat.getID(), info.result.username)


# Delete all the commands in the bot
@bot.add_regex_helper(regex="^delete my command$")
def send_bold(message: Message):
    response = bot.delete_my_commands()
    print(response.to_dict())


# Printing the commands
print(bot.get_my_commands().to_dict())

# To starting the bot listening
bot.poll(update=update)
