# TelegramBot

## Project Description

This project uses the telegram bot API to create a bot service

## Installation

To install with pip <br>

```
$ pip install Telegram-Bot8
```

## Usage

```python
from Bot.TeleBot import TeleBot

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

## Credits

<table>
  <tr>
        <td align="center"><a href="https://github.com/appdevin"><img src="https://avatars1.githubusercontent.com/u/34540492?s=460&u=6b2d7e8346afc28bfd8e591d93fd548895c720af&v=4" width="100px;" alt=""/><br /><sub><b>Jeyavishnu</b></sub></a><br />
    </td>
  </tr>
</table>

## License

Distributed under the MIT License. See `LICENSE` for more information.
