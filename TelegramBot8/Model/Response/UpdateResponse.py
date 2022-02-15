import json
from enum import Enum
from typing import Any, Optional, List, TypeVar, Type, cast

from . import from_int, from_str, from_list, from_bool, from_union, from_none, to_class


class Chat:
    id: int
    first_name: Optional[str]
    username: Optional[str]
    type: str
    title: Optional[str]
    all_members_are_administrators: Optional[bool]

    def __init__(self, id: int, first_name: Optional[str], username: Optional[str], type: str, title: Optional[str], all_members_are_administrators: Optional[bool]) -> None:
        self.id = id
        self.first_name = first_name
        self.username = username
        self.type = type
        self.title = title
        self.all_members_are_administrators = all_members_are_administrators

    @staticmethod
    def from_dict(obj: Any) -> 'Chat':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        first_name = from_union([from_str, from_none], obj.get("first_name"))
        username = from_union([from_str, from_none], obj.get("username"))
        type = from_str(obj.get("type"))
        title = from_union([from_str, from_none], obj.get("title"))
        all_members_are_administrators = from_union([from_bool, from_none], obj.get("all_members_are_administrators"))
        return Chat(id, first_name, username, type, title, all_members_are_administrators)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["first_name"] = from_union([from_str, from_none], self.first_name)
        result["username"] = from_union([from_str, from_none], self.username)
        result["type"] = from_str(self.type)
        result["title"] = from_union([from_str, from_none], self.title)
        result["all_members_are_administrators"] = from_union([from_bool, from_none], self.all_members_are_administrators)
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
        result: dict = {}
        result["offset"] = from_int(self.offset)
        result["length"] = from_int(self.length)
        result["type"] = from_str(self.type)
        return result



class From:
    id: int
    is_bot: bool
    first_name: str
    username: str
    language_code: Optional[str]

    def __init__(self, id: int, is_bot: bool, first_name: str, username: str, language_code: Optional[str]) -> None:
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
        language_code = from_union([from_str, from_none], obj.get("language_code"))
        return From(id, is_bot, first_name, username, language_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["is_bot"] = from_bool(self.is_bot)
        result["first_name"] = from_str(self.first_name)
        result["username"] = from_str(self.username)
        result["language_code"] = from_union([from_str, from_none], self.language_code)
        return result

class Message:
    message_id: int
    message_from: From
    chat: Chat
    date: int
    text: Optional[str]
    entities: Optional[List[Entity]]
    new_chat_participant: Optional[From]
    new_chat_member: Optional[From]
    new_chat_members: Optional[List[From]]

    def __init__(self, message_id: int, message_from: From, chat: Chat, date: int, text: Optional[str],
                 entities: Optional[List[Entity]], new_chat_participant: Optional[From],
                 new_chat_member: Optional[From], new_chat_members: Optional[List[From]]) -> None:
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
        message_from = From.from_dict(obj.get("from"))
        chat = Chat.from_dict(obj.get("chat"))
        date = from_int(obj.get("date"))
        text = from_union([from_str, from_none], obj.get("text"))
        entities = from_union([lambda x: from_list(Entity.from_dict, x), from_none], obj.get("entities"))
        new_chat_participant = from_union([From.from_dict, from_none], obj.get("new_chat_participant"))
        new_chat_member = from_union([From.from_dict, from_none], obj.get("new_chat_member"))
        new_chat_members = from_union([lambda x: from_list(From.from_dict, x), from_none], obj.get("new_chat_members"))
        return Message(message_id, message_from, chat, date, text, entities, new_chat_participant, new_chat_member,
                       new_chat_members)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message_id"] = from_int(self.message_id)
        result["from"] = to_class(From, self.message_from)
        result["chat"] = to_class(Chat, self.chat)
        result["date"] = from_int(self.date)
        result["text"] = from_union([from_str, from_none], self.text)
        result["entities"] = from_union([lambda x: from_list(lambda x: to_class(Entity, x), x), from_none],
                                        self.entities)
        result["new_chat_participant"] = from_union([lambda x: to_class(From, x), from_none], self.new_chat_participant)
        result["new_chat_member"] = from_union([lambda x: to_class(From, x), from_none], self.new_chat_member)
        result["new_chat_members"] = from_union([lambda x: from_list(lambda x: to_class(From, x), x), from_none],
                                                self.new_chat_members)
        return result


class Update:
    update_id: int
    message: Message

    def __init__(self, update_id: int, message: Message) -> None:
        self.update_id = update_id
        self.message = message

    def getNextUpdateID(self) -> int:
        return self.update_id + 1

    @staticmethod
    def from_dict(obj: Any) -> 'Update':
        assert isinstance(obj, dict)
        update_id = from_int(obj.get("update_id"))
        message = Message.from_dict(obj.get("message"))
        return Update(update_id, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["update_id"] = from_int(self.update_id)
        result["message"] = to_class(Message, self.message)
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
