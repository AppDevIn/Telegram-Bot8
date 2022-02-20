import json
from typing import Any, Optional

from . import Message, from_union, from_none, from_bool, to_class, BaseResponse


class PhotoResponse(BaseResponse):
    ok: bool
    result: Message

    def __init__(self, ok: Optional[bool], result: Optional[Message]) -> None:
        self.ok = ok
        self.result = result

    @staticmethod
    def cast(obj: 'BaseResponse') -> 'PhotoResponse':
        try:
            return PhotoResponse.from_dict(obj.to_dict())
        except Exception:
            raise ReferenceError

    @staticmethod
    def from_dict(obj: Any) -> 'PhotoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        result = from_union([Message.from_dict, from_none], obj.get("result"))
        return PhotoResponse(ok, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["result"] = from_union([lambda x: to_class(Message, x), from_none], self.result)
        return result


def photo_response_from_dict(s: Any) -> PhotoResponse:
    data = json.loads(s)
    return PhotoResponse.from_dict(data)


class AudioResponse(BaseResponse):
    ok: bool
    result: Message

    def __init__(self, ok: bool, result: Message) -> None:
        self.ok = ok
        self.result = result

    @staticmethod
    def cast(obj: 'BaseResponse') -> 'AudioResponse':
        try:
            return AudioResponse.from_dict(obj.to_dict())
        except Exception:
            raise ReferenceError

    @staticmethod
    def from_dict(obj: Any) -> 'AudioResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        result = from_union([Message.from_dict, from_none], obj.get("result"))
        return AudioResponse(ok, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["result"] = from_union([lambda x: to_class(Message, x), from_none], self.result)
        return result


def audio_response_from_dict(s: Any) -> AudioResponse:
    data = json.loads(s)
    return AudioResponse.from_dict(data)