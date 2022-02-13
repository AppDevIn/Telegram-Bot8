import json
from enum import Enum
from typing import Any, Optional, List, TypeVar, Type, cast

from . import from_int, from_str, from_list, from_bool, from_union, from_none, to_class


class Chat:
    id: int
    first_name: str
    username: str
    type: str

    def __init__(self, id: int, first_name: str, username: str, type: str) -> None:
        self.id = id
        self.first_name = first_name
        self.username = username
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Chat':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        first_name = from_str(obj.get("first_name"))
        username = from_str(obj.get("username"))
        type = from_str(obj.get("type"))
        return Chat(id, first_name, username, type)

    def to_dict(self) -> dict:
        result: dict = {
            "id": from_int(self.id),
            "first_name": from_str(self.first_name),
            "username": from_str(self.username),
            "type": from_str(self.type)
        }
        return result


class Entity:
    offset: int
    length: int
    type: str

    def __init__(self, offset: int, length: int, type: str) -> None:
        self.offset = offset
        self.length = length
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Entity':
        assert isinstance(obj, dict)
        offset = from_int(obj.get("offset"))
        length = from_int(obj.get("length"))
        type = from_str(obj.get("type"))
        return Entity(offset, length, type)

    def to_dict(self) -> dict:
        result: dict = {
            "offset": from_int(self.offset),
            "length": from_int(self.length),
            "type": from_str(self.type)
        }
        return result


class From:
    id: int
    is_bot: bool
    first_name: str
    username: str
    language_code: str

    def __init__(self, id: int, is_bot: bool, first_name: str, username: str, language_code: str) -> None:
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.username = username
        self.language_code = language_code

    @staticmethod
    def from_dict(obj: Any) -> 'From':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        is_bot = from_bool(obj.get("is_bot"))
        first_name = from_str(obj.get("first_name"))
        username = from_str(obj.get("username"))
        language_code = from_str(obj.get("language_code"))
        return From(id, is_bot, first_name, username, language_code)

    def to_dict(self) -> dict:
        result: dict = {
            "id": from_int(self.id),
            "is_bot": from_bool(self.is_bot),
            "first_name": from_str(self.first_name),
            "username": from_str(self.username),
            "language_code": from_str(self.language_code)
        }
        return result


class Message:
    message_id: int
    message_from: From
    chat: Chat
    date: int
    text: str
    entities: Optional[List[Entity]]

    def __init__(self, message_id: int, message_from: From, chat: Chat, date: int, text: str, entities: Optional[List[Entity]]) -> None:
        self.message_id = message_id
        self.message_from = message_from
        self.chat = chat
        self.date = date
        self.text = text
        self.entities = entities

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        message_id = from_int(obj.get("message_id"))
        message_from = From.from_dict(obj.get("from"))
        chat = Chat.from_dict(obj.get("chat"))
        date = from_int(obj.get("date"))
        text = from_str(obj.get("text"))
        entities = from_union([lambda x: from_list(Entity.from_dict, x), from_none], obj.get("entities"))
        return Message(message_id, message_from, chat, date, text, entities)

    def to_dict(self) -> dict:
        result: dict = {
            "message_id": from_int(self.message_id),
            "from": to_class(From, self.message_from),
            "chat": to_class(Chat, self.chat),
            "date": from_int(self.date),
            "text": from_str(self.text),
            "entities": from_union([lambda x: from_list(lambda x: to_class(Entity, x), x), from_none], self.entities)
        }
        return result


class Update:
    update_id: int
    message: Message

    def __init__(self, update_id: int, message: Message) -> None:
        self.update_id = update_id
        self.message = message

    def getNextUpdateID(self):
        return self.update_id + 1



    @staticmethod
    def from_dict(obj: Any) -> 'Update':
        assert isinstance(obj, dict)
        update_id = from_int(obj.get("update_id"))
        message = Message.from_dict(obj.get("message"))
        return Update(update_id, message)

    def to_dict(self) -> dict:
        result: dict = {
            "update_id": from_int(self.update_id),
            "message": to_class(Message, self.message)
        }
        return result


class UpdateList:
    ok: bool
    result: List[Update]

    def __init__(self, ok: bool, result: List[Update]) -> None:
        self.ok = ok
        self.result = result

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateList':
        assert isinstance(obj, dict)
        ok = from_bool(obj.get("ok"))
        result = from_list(Update.from_dict, obj.get("result"))
        return UpdateList(ok, result)

    def to_dict(self) -> dict:
        result: dict = {
            "ok": from_bool(self.ok),
            "result": from_list(lambda x: to_class(Update, x), self.result)
        }
        return result


def update_list_from_dict(s: Any) -> UpdateList:
    data = json.loads(s)
    return UpdateList.from_dict(data)


def update_list_to_dict(x: UpdateList) -> Any:
    return to_class(UpdateList, x)



class ParseMode(Enum):
    MarkdownV2 = "MarkdownV2"
    Markdown = "MarkdownV2"
    HTML = "html"