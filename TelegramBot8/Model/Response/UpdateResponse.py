import json
from enum import Enum
from typing import Any, Optional, List, TypeVar, Type, cast

from . import from_int, from_str, from_list, from_bool, from_union, from_none, to_class


class Chat:
    id: int
    type: str
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    all_members_are_administrators: Optional[bool]

    def __init__(self, id: int, type: Optional[str], first_name: Optional[str] = None, username: Optional[str] = None,
                 title: Optional[str] = None, all_members_are_administrators: Optional[bool] = None) -> None:
        self.id = id
        self.first_name = first_name
        self.username = username
        self.type = type
        self.title = title
        self.all_members_are_administrators = all_members_are_administrators

    @staticmethod
    def from_dict(obj: Any) -> 'Chat':
        assert isinstance(obj, dict)
        id = obj.get("id")
        type = from_str(obj.get("type"))
        first_name = from_union([from_str, from_none], obj.get("first_name"))
        username = from_union([from_str, from_none], obj.get("username"))
        title = from_union([from_str, from_none], obj.get("title"))
        all_members_are_administrators = from_union([from_bool, from_none], obj.get("all_members_are_administrators"))
        return Chat(id, first_name, username, type, title, all_members_are_administrators)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = self.id
        result["first_name"] = from_union([from_str, from_none], self.first_name)
        result["username"] = from_union([from_str, from_none], self.username)
        result["type"] = from_union([from_str, from_none], self.type)
        result["title"] = from_union([from_str, from_none], self.title)
        result["all_members_are_administrators"] = from_union([from_bool, from_none], self.all_members_are_administrators)
        return result


class MessageEntity:
    offset: int
    length: int
    type: str

    def __init__(self, offset: int, length: int, type: str) -> None:
        self.offset = offset
        self.length = length
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'MessageEntity':
        assert isinstance(obj, dict)
        offset = from_int(obj.get("offset"))
        length = from_int(obj.get("length"))
        type = from_str(obj.get("type"))
        return MessageEntity(offset, length, type)

    def to_dict(self) -> dict:
        result: dict = {"offset": from_int(self.offset),
                        "length": from_int(self.length),
                        "type": from_str(self.type)
                        }
        return result


class User:
    id: int
    is_bot: bool
    first_name: str
    username: Optional[str]
    language_code: Optional[str]

    def __init__(self, id: int, is_bot: bool, first_name: str, username: Optional[str],
                 language_code: Optional[str]) -> None:
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.username = username
        self.language_code = language_code

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        is_bot = from_bool(obj.get("is_bot"))
        first_name = from_str(obj.get("first_name"))
        username = from_union([from_str, from_none], obj.get("username"))
        language_code = from_union([from_str, from_none], obj.get("language_code"))
        return User(id, is_bot, first_name, username, language_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["is_bot"] = from_union([from_bool, from_none], self.is_bot)
        result["first_name"] = from_union([from_str, from_none], self.first_name)
        result["username"] = from_union([from_str, from_none], self.username)
        result["language_code"] = from_union([from_str, from_none], self.language_code)
        return result


class Message:
    message_id: int
    message_from: Optional[User]
    chat: Optional[Chat]
    date: int
    text: Optional[str]
    entities: Optional[List[MessageEntity]]
    new_chat_participant: Optional[User]
    new_chat_member: Optional[User]
    new_chat_members: Optional[List[User]]

    def __init__(self, message_id: int, message_from: Optional[User], chat: Optional[Chat],
                 date: Optional[int], text: Optional[str], entities: Optional[List[MessageEntity]],
                 new_chat_participant: Optional[User], new_chat_member: Optional[User],
                 new_chat_members: Optional[List[User]]) -> None:
        self.message_id = message_id
        self.message_from = message_from
        self.chat = chat
        self.date = date
        self.text = text
        self.entities = entities
        self.new_chat_participant = new_chat_participant
        self.new_chat_member = new_chat_member
        self.new_chat_members = new_chat_members

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        message_id = from_int(obj.get("message_id"))
        message_from = from_union([User.from_dict, from_none], obj.get("from"))
        chat = from_union([Chat.from_dict, from_none], obj.get("chat"))
        date = from_int(obj.get("date"))
        text = from_union([from_str, from_none], obj.get("text"))
        entities = from_union([lambda x: from_list(MessageEntity.from_dict, x), from_none], obj.get("entities"))
        new_chat_participant = from_union([User.from_dict, from_none], obj.get("new_chat_participant"))
        new_chat_member = from_union([User.from_dict, from_none], obj.get("new_chat_member"))
        new_chat_members = from_union([lambda x: from_list(User.from_dict, x), from_none], obj.get("new_chat_members"))
        return Message(message_id, message_from, chat, date, text, entities, new_chat_participant, new_chat_member,
                       new_chat_members)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message_id"] = from_int(self.message_id)
        result["from"] = from_union([lambda x: to_class(User, x), from_none], self.message_from)
        result["chat"] = from_union([lambda x: to_class(Chat, x), from_none], self.chat)
        result["date"] = from_int(self.date)
        result["text"] = from_union([from_str, from_none], self.text)
        result["entities"] = from_union([lambda x: from_list(lambda x: to_class(MessageEntity, x), x), from_none],
                                        self.entities)
        result["new_chat_participant"] = from_union([lambda x: to_class(User, x), from_none], self.new_chat_participant)
        result["new_chat_member"] = from_union([lambda x: to_class(User, x), from_none], self.new_chat_member)
        result["new_chat_members"] = from_union([lambda x: from_list(lambda x: to_class(User, x), x), from_none],
                                                self.new_chat_members)
        return result


class Update:
    update_id: int
    message: Optional[Message]

    def __init__(self, update_id: int, message: Optional[Message]) -> None:
        self.update_id = update_id
        self.message = message

    def getNextUpdateID(self) -> int:
        return self.update_id + 1

    @staticmethod
    def from_dict(obj: Any) -> 'Update':
        assert isinstance(obj, dict)
        update_id = from_int(obj.get("update_id"))
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        return Update(update_id, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["update_id"] = from_int(self.update_id)
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        return result


class UpdateList:
    ok: bool
    result: List[Update]
    _ori_dict = {}

    def __init__(self, ok: bool, result: List[Update], original: {}) -> None:
        self.ok = ok
        self.result = result
        self._ori_dict = original

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateList':
        assert isinstance(obj, dict)
        ok = from_bool(obj.get("ok"))
        result = from_list(Update.from_dict, obj.get("result"))
        return UpdateList(ok, result, obj)

    def to_dict(self) -> dict:
        result: dict = {
            "ok": from_bool(self.ok),
            "result": from_list(lambda x: to_class(Update, x), self.result)
        }
        result.update(self._ori_dict)
        return result


def update_list_from_dict(s: Any) -> UpdateList:
    data = json.loads(s)
    print(data)
    return UpdateList.from_dict(data)


def update_list_to_dict(x: UpdateList) -> Any:
    return to_class(UpdateList, x)


class ParseMode(Enum):
    MarkdownV2 = "MarkdownV2"
    Markdown = "MarkdownV2"
    HTML = "html"
