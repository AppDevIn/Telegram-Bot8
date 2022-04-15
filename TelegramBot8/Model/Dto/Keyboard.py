import json

from ..Reqest import BaseRequest


class Keyboard:
    body = {}

    def __init__(self):
        self.body = {}

    def addParameter(self, key, value, not_required=False) -> {}:
        if not_required or None is value:
            return self.body
        self.body[key] = value
        return self.body

    def to_dict(self):
        return self.body

    def to_json(self):
        return json.dumps(self.body)


# TODO: Add login_url and callback_game
class InlineKeyboardButton(Keyboard):

    def __init__(self, text, url=None, callback_data=None, switch_inline_query=None,
                 switch_inline_query_current_chat=None, pay=None):
        super(InlineKeyboardButton, self).__init__()
        self.addParameter("text", text)
        self.addParameter("url", url)
        self.addParameter("callback_data", callback_data)
        self.addParameter("switch_inline_query", switch_inline_query)
        self.addParameter("switch_inline_query_current_chat", switch_inline_query_current_chat)
        self.addParameter("pay", pay)


class InlineKeyboard(Keyboard):

    def __init__(self):
        super(InlineKeyboard, self).__init__()
        self.list = []

    def add(self, *keyboards):
        listKeyboard = list(map(lambda k: k.to_dict(), keyboards))
        self.list.append(listKeyboard)

    def to_dict(self):
        return {"inline_keyboard": self.list}

    def to_json(self):
        return json.dumps({"inline_keyboard": self.list})
