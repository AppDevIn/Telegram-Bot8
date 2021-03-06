from ..Dto import User
from ..Response import Message


class CallbackMessage(object):

    def __init__(self, response):
        super().__init__()

        self._id = response["id"]
        self.message = Message(response=response["message"])
        self._chat_instance = response["chat_instance"]
        self._data = response["data"]
        self.fromUser = User(response["from"])
