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


@bot.add_command_menu_helper(command="/sendaudio", description="Send audio")
def sendAudio(message: Message):
    # To send image using file
    # response: BaseResponse = bot.send_audio(message.chat.id, file="/Users/jeyavishnu/Downloads/audio.mp3")
    response: BaseResponse = bot.send_audio(message.chat.id,
                                            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    if response.status_code == 200:
        response: MediaResponse = MediaResponse.cast(response)
    else:
        print(response.to_dict())


@bot.add_command_menu_helper(command="/senddocument", description="Send document")
def sendDocument(message: Message):
    # To send image using file
    response: BaseResponse = bot.send_document(message.chat.id, file="/Users/jeyavishnu/Downloads/Weekly_Report_Jeyavishnu_Week_19.docx")
    # response: BaseResponse = bot.send_document(message.chat.id,
    #                                            document_url="https://learn-ap-southeast-1-prod-fleet02-xythos.content.blackboardcdn.com/5dfa8616972ac/4057111?X-Blackboard-Expiration=1645380000000&X-Blackboard-Signature=LaGQRsOIjcfNeey7Vz81AVef6niIucY7E6zMc%2Fi3AxY%3D&X-Blackboard-Client-Id=180274&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27Final%2520Report%2520Assessment%2520Criteria.pdf&response-content-type=application%2Fpdf&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDmFwLXNvdXRoZWFzdC0xIkcwRQIgJOAunv7jLfICaIl%2BSZ3ahc7I6pV9OQ1kJI9UW%2BZE3t0CIQDAFnaOK1HZ1PLve8geweIqSOlegtcerQlp4hC085uJQSqEBAgtEAIaDDYzNTU2NzkyNDE4MyIM8GdDhlCK8Np2Jv9AKuEDiTB0Sxa9KziZ0d6AbvSnfoPXYNB%2FKvAhOgJeuFALK2IwqINzbM6J8OrfcqpqhpY5SEqyRvkcMaBvKeK4vsyccXedjfMIeVHYAQL%2BwEyQl3rZ%2FIsIAW6G7%2F2knsFOZyjl03D1eRPkY93hlCe0eRHgfeqEJu%2F5CHyGoyfgaROdjJEjWrbA3Nt%2BPqwJeu8JN7Mc9SM2XtBHQbrXLKSdDn1ENMRc0ogSei1rlaP6XHfQGRIz9fCPwgGxpdyh1G4gnJJWL5buf22MPzsPM3AG8ZTXXpcvFKmDIBfemCqI0br1EJ%2FuytKFwPdGkCU6KumbmIEJtHZiSPE6E2O5lulwlFKTHYDHFOjFBa%2B8lfgBYN8zjcV4xKUMOZUIiha3gTpZt3Pq3jE1iS8xThYiq9HkcwXFvdGiyog8L7VRkEBvVvofiRXWGlECiGOzMES8R7zAEuA%2FAgPzhloj1yLZToGWBEBrGLeJ3IJxhDNv02qL7NaEdVci%2BsNq5%2Bap98Q%2F8tWzN6KklYtVQUmocG%2Bxk426U8kdjDZsdHARqqFWZjhpT1E1Qegrv0NvdCAJ9J6PArqjpyRTmZwpln4EKd3vDLWaww%2Fjts%2FU%2FpaQjA9R6kJ6AMGLhDJOPmnSF0jVvWf27jgVYu91GzD74ciQBjqlAaJuRHPmKbbHk7%2B%2FrMwshlSbJLwONZZ2q8qG4oMct6yiIVKGg%2BmnPbAuBX12yNBELEFiFW4RSlx83F2xze9hYzaKKSl2n9S5hYc5QDXZ0DHORcsc8SFyiELCFZSVmVG7U1eoKNdVDSxiqAIt%2BUEHZXkXg9sK3%2B%2BS2BD%2Fq9PSkRxssKVJZXSG8PdG8t1%2BBD2%2FqkBWcLj5CyX9aBZUSw3SgAlDt2TJFw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220220T120000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIAZH6WM4PL673JSHGX%2F20220220%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Signature=0c89d1f2c742f181c75ec0238eb637ee850463b0d7afed6c5c622b55f52455bd")
    if response.status_code == 200:
        response: MediaResponse = MediaResponse.cast(response)
    else:
        print(response.to_dict())


# Printing the commands
print(bot.get_my_commands().to_dict())

# To starting the bot listening
bot.poll(update=update)
print("Hello from below")
