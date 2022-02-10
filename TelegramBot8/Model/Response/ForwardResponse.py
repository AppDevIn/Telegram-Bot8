import json
from typing import Any, Optional

from . import from_int, from_bool, from_str, to_class, from_union, from_none


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
        result: dict = {}
        result["id"] = from_int(self.id)
        result["first_name"] = from_str(self.first_name)
        result["username"] = from_str(self.username)
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


class Result:
    message_id: int
    result_from: From
    chat: Chat
    date: int
    forward_from: From
    forward_date: int
    text: str

    def __init__(self, message_id: int, result_from: From, chat: Chat, date: int, forward_from: From, forward_date: int,
                 text: str) -> None:
        self.message_id = message_id
        self.result_from = result_from
        self.chat = chat
        self.date = date
        self.forward_from = forward_from
        self.forward_date = forward_date
        self.text = text

    @staticmethod
    def from_dict(obj: Any) -> 'SetMyCommandRequest':
        assert isinstance(obj, dict)
        message_id = from_int(obj.get("message_id"))
        result_from = From.from_dict(obj.get("from"))
        chat = Chat.from_dict(obj.get("chat"))
        date = from_int(obj.get("date"))
        forward_from = From.from_dict(obj.get("forward_from"))
        forward_date = from_int(obj.get("forward_date"))
        text = from_str(obj.get("text"))
        return Result(message_id, result_from, chat, date, forward_from, forward_date, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message_id"] = from_int(self.message_id)
        result["from"] = to_class(From, self.result_from)
        result["chat"] = to_class(Chat, self.chat)
        result["date"] = from_int(self.date)
        result["forward_from"] = to_class(From, self.forward_from)
        result["forward_date"] = from_int(self.forward_date)
        result["text"] = from_str(self.text)
        return result


class ForwardResponse:
    ok: bool
    result: Result

    def __init__(self, ok: bool, result: Result) -> None:
        self.ok = ok
        self.result = result

    @staticmethod
    def from_dict(obj: Any) -> 'ForwardResponse':
        assert isinstance(obj, dict)
        ok = from_bool(obj.get("ok"))
        result = Result.from_dict(obj.get("result"))
        return ForwardResponse(ok, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_bool(self.ok)
        result["result"] = to_class(Result, self.result)
        return result


def forward_from_dict(s: Any) -> ForwardResponse:
    data = json.loads(s)
    return ForwardResponse.from_dict(data)


def forward_to_dict(x: ForwardResponse) -> Any:
    return to_class(ForwardResponse, x)
