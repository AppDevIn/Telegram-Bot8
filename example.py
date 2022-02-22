import os

from TelegramBot8 import Message, TeleBot, ParseMode, Update, BotCommandScope, MediaResponse, Error, BaseResponse

API_KEY = os.getenv('telegramApiKey')
bot = TeleBot(API_KEY)


# Just listening to updated
def update(data: Update):
    # print(data.to_dict())
    print(f"User {data.message.message_from.id} has entered {data.message.text}")


# Adds command into telegram menu and listen to multiple commands
@bot.add_command_menu_helper(command=["/hello", "/hallo"], description="Trigger hello message")
def endServer(message: Message):
    bot.send_message(message.chat.id, "Hello")


# Just listens to commands
@bot.add_command_helper(command="/hi")
def endServer(message: Message):
    bot.send_message(message.chat.id, "Hello")


# Listens to single command
@bot.add_command_menu_helper(command="/bye", description="Trigger the bye message")
def endServer(message: Message):
    bot.send_message(message.chat.id, "Bye")


# Adding command to groups only
@bot.add_command_menu_helper(command="/group", description="Trigger the group bye",
                             scope=BotCommandScope.BotCommandScopeAllGroupChats())
def endServer(message: Message):
    bot.send_message(message.chat.id, "Bye")


# Listen to regex based messages
@bot.add_regex_helper(regex="^hi$")
def endServer(message: Message):
    bot.send_message(message.chat.id, "Hello")


# Sending bold message and types is possible
@bot.add_regex_helper(regex="^bold$")
def send_bold(message: Message):
    bot.send_message(message.chat.id, "<b>Hello</b>", parse_mode=ParseMode.HTML)


# Forwarding message in telegram bot
@bot.add_regex_helper(regex=["^forward message$", "^fwd message$"])
def send_bold(message: Message):
    print(bot.forward_messaged(chat_id=message.chat.id, from_chat_id=message.chat.id,
                               message_id=message.message_id))


# Getting information about the bot"
@bot.add_regex_helper(regex="^get me$")
def send_bold(message: Message):
    info = bot.get_me()
    bot.send_message(message.chat.id, info.result.username)


# Delete all the commands in the bot
@bot.add_regex_helper(regex="^delete my command$")
def send_bold(message: Message):
    response = bot.delete_my_commands()
    print(response.to_dict())


# Command to send photo
@bot.add_command_menu_helper(command="/sendphoto", description="Send photo")
def sendPhoto(message: Message):
    # To send image using file
    # response: BaseResponse = bot.send_photo(message.chat.id, file="/Users/jeyavishnu/Downloads/profile.png")
    response: BaseResponse = bot.send_photo(message.chat.id,
                                            image_url="https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg")
    if response.status_code == 200:
        response: MediaResponse = MediaResponse.cast(response)
    else:
        print(response.to_dict())


# Command to send audio
@bot.add_command_menu_helper(command="/sendaudio", description="Send audio")
def sendAudio(message: Message):
    # To send audio using file
    # response: BaseResponse = bot.send_audio(message.chat.id, file="/Users/jeyavishnu/Downloads/audio.mp3")
    response: BaseResponse = bot.send_audio(message.chat.id,
                                            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    if response.status_code == 200:
        response: MediaResponse = MediaResponse.cast(response)
    else:
        print(response.to_dict())


# Command to send document
@bot.add_command_menu_helper(command="/senddocument", description="Send document")
def sendDocument(message: Message):
    # To send document using file
    # response: BaseResponse = bot.send_document(message.chat.id, file="/Users/jeyavishnu/Downloads/some-doc.docx")
    response: BaseResponse = bot.send_document(message.chat.id, document_url="URL_TO_DOC")
    if response.status_code == 200:
        response: MediaResponse = MediaResponse.cast(response)
    else:
        print(response.to_dict())


# Command to send video
@bot.add_command_menu_helper(command="/sendvideo", description="Send Video")
def sendVideo(message: Message):
    # To send video using file
    response: BaseResponse = bot.send_video(message.chat.id, file="/Users/jeyavishnu/Downloads/strange.mp4")
    # response: BaseResponse = bot.send_video(message.chat.id, video_url="https://t.me/TelegramTips/320")
    if response.status_code == 200:
        response: MediaResponse = MediaResponse.cast(response)
    else:
        print(response.to_dict())


# Printing the commands
print(bot.get_my_commands().to_dict())

# To starting the bot listening
bot.poll(update=update)
print("Hello from below")
