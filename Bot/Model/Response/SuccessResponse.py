# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = success_from_dict(json.loads(json_string))
import json
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Success:
    ok: bool
    result: bool

    def __init__(self, ok: bool, result: bool) -> None:
        self.ok = ok
        self.result = result

    @staticmethod
    def from_dict(obj: Any) -> 'Success':
        assert isinstance(obj, dict)
        ok = from_bool(obj.get("ok"))
        result = from_bool(obj.get("result"))
        return Success(ok, result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_bool(self.ok)
        result["result"] = from_bool(self.result)
        return result


def success_from_dict(s: Any) -> Success:
    data = json.loads(s)
    return Success.from_dict(data)


def success_to_dict(x: Success) -> Any:
    return to_class(Success, x)
