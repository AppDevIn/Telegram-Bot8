# TelegramBot

## Project Description

This project uses the telegram bot API to create a bot service

## Installation

To install with pip <br>

```
$ python -m pip install repo_helper_github
```

## Usage

```python
from TeleBot import TeleBot

@bot.add_command_helper(command="/hi")
def hi(message: Message):
    bot.send_message(message.chat.getID(), "Hello")


@bot.add_command_menu_helper(command="/bye", description="Just testing added command")
def bye(message: Message):
    bot.send_message(message.chat.getID(), "Bye")


@bot.add_regex_helper(regex="^hi$")
def regex(message: Message):
    bot.send_message(message.chat.getID(), "Hello")

bot.poll()
```
