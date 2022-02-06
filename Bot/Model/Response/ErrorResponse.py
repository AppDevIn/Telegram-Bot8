import json
from typing import Any, TypeVar

from Bot.Model.Response.BaseConvertors import from_bool, from_int, from_str, to_class

T = TypeVar("T")


class Error:
    ok: bool
    error_code: int
    description: str

    def __init__(self, ok: bool, error_code: int, description: str) -> None:
        self.ok = ok
        self.error_code = error_code
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        ok = from_bool(obj.get("ok"))
        error_code = from_int(obj.get("error_code"))
        description = from_str(obj.get("description"))
        return Error(ok, error_code, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_bool(self.ok)
        result["error_code"] = from_int(self.error_code)
        result["description"] = from_str(self.description)
        return result


def error_from_dict(s: Any) -> Error:
    data = json.loads(s)
    return Error.from_dict(data)


def error_to_dict(x: Error) -> Any:
    return to_class(Error, x)
