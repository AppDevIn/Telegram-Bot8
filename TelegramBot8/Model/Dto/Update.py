from enum import Enum

from . import Message, CallbackMessage


class UpdateType(Enum):
    MESSAGE = "message"
    CALLBACK = "callback_query"
    EDITED_CHANNEL_POST = "edited_channel_post"


class Update(object):
    _update_id = int()
    _hasCallback = True
    _hasMessage = True

    def __init__(self, response):
        super().__init__()
        self._update_id = int(response["update_id"])

        try:
            self.message = Message(response["message"])
        except Exception as e:
            self._hasMessage = False

        try:
            self.callback = CallbackMessage(response["callback_query"])
        except KeyError:
            self._hasCallback = False

    def getUpdateType(self) -> UpdateType:

        if self._hasMessage:
            return UpdateType.MESSAGE
        elif self._hasCallback:
            return UpdateType.CALLBACK

    def getNextUpdateID(self):
        return self._update_id + 1

    def hasMessage(self) -> bool:
        return self._hasMessage

    def hasCallback(self) -> bool:
        return self._hasMessage

    def getMessage(self) -> Message:
        if self._hasMessage:
            return self.message
        else:
            raise ValueError

    def getCallback(self) -> Message:
        if self._hasCallback:
            return self.callback
        else:
            raise ValueError
