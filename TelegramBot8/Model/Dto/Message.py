from .User import User
from .Chat import Chat
from .Entities import Entities
from .InlineKeyboard import InlineKeyboard
from enum import Enum


class Message(object):
    _message_id = int()
    date = int()
    text = str()
    _entities = True

    def __init__(self, response):
        super().__init__()
        self._message_id = response["message_id"]
        self.fromUser = User(response["from"])
        self.chat = Chat(response["chat"])
        self.date = response["date"]
        self.entities = []

        try:
            self.text = response["text"]
        except:
            self.text = ""

        try:
            self.replyMarkup = InlineKeyboard(response=response["reply_markup"]["inline_keyboard"])
        except KeyError:
            self.replyMarkup = None

        try:
            for item in response["entities"]:
                self.entities.append(Entities(item))
        except:
            self._entities = False

    def entityType(self) -> bool:
        return self._entities

    def get_id(self):
        return self._message_id


class ParseMode(Enum):
    MarkdownV2 = "MarkdownV2"
    Markdown = "MarkdownV2"
    HTML = "html"
