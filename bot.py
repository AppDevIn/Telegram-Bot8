from typing import List
import requests
import json
import model.Constants as const

from model.Update import UpdateType, Update


class TeleBot:
    _commands = {}
    _callback = {}

    def __init__(self, token):
        self.base = f"{const.BASE_URL}{token}/"

    def poll(self):
        lastUpdate = None
        while True:
            if lastUpdate is None:
                response = self.get_updates(offset=-1)
            else:
                response = self.get_updates(offset=lastUpdate.getNextUpdateID())

            updates = self.generate_updates(response)

            if updates:
                for item in updates:
                    lastUpdate = item
                    self.process_update(item)

    def add_command(self, command):
        def decorator(func):
            self._commands[command] = func

        return decorator

    def add_callback(self, callback_data):
        def decorator(func):
            self._callback[callback_data] = func

        return decorator

    def get_updates(self, offset=None, timeout=1200, allowed_types=None) -> {}:
        if allowed_types is None:
            allowed_types = [UpdateType.MESSAGE]

        get_update_url = UpdateUrl(self.base) \
            .timeout(timeout) \
            .allowed_updates(allowed_types) \
            .offset(offset, condition=offset is not None) \
            .build()

        response = requests.request("GET", get_update_url, headers={}, data={})
        response = json.loads(response.content)["result"]

        return response

    def generate_updates(self, response) -> List[Update]:

        if response.get('ok', False) is True:
            return list(map(lambda update: Update(response=update), response))
        else:
            raise ValueError(response['error'])

    def process_update(self, item):
        if item.getUpdateType() == UpdateType.MESSAGE and item.message.entityType():
            command = item.message.text[item.message.entities[0].offset:item.message.entities[0].length]
            if self._commands.get(command): self._commands.get(command)(item)
        elif item.getUpdateType() == UpdateType.CALLBACK:
            callback = item.callback.message.replyMarkup.keyboards[0].callbackData.split("@")[1]
            self._callback.get(callback)(item)

    def send_message(self, chat_id, text):
        url = self.base + f"sendMessage?chat_id={chat_id}&text={text}"
        requests.request("POST", url, headers={}, data={})

    def send_callback(self, chat_id, text, replyMarkUp):
        url = self.base + f"sendMessage?chat_id={chat_id}&text={text}&reply_markup={replyMarkUp}"
        requests.request("POST", url, headers={}, data={})

    def send_photo(self, chat_id, file):
        up = {'photo': ("i.png", open(file, 'rb'), "multipart/form-data")}
        url = self.base + f"sendPhoto"
        requests.post(url, files=up, data={
            "chat_id": chat_id,
        })


class UrlBuilder:
    def __init__(self, base):
        self.base = base
        self.firstParameter = True

    def addParameter(self, value) -> str:
        if self.firstParameter is True:
            self.firstParameter = False
            self.base += f"?{value}"
        else:
            self.base += f"&{value}"
        return self.base

    def build(self) -> str:
        return self.base


class UpdateUrl(UrlBuilder):

    def __init__(self, url):
        self.base = url + "getUpdates"
        super(UpdateUrl, self).__init__(self.base)

    def timeout(self, timeout):
        self.addParameter(f"timeout={timeout}")
        return self

    def offset(self, offset, condition=True):
        if condition:
            self.addParameter(f"offset={offset}")
        return self

    def allowed_updates(self, allowed_updates: []):
        self.addParameter(f"allowed_updates={allowed_updates}")
        return self

    def limit(self, limit: int):
        self.addParameter(f"limit={limit}")
        return self
