from typing import List
import re
import requests
import json
import model.Constants as const
from url.UrlBuilder import UpdateUrl

from model.Update import UpdateType, Update


class TeleBot:
    _commands = {}
    _callback = {}
    _text = {}

    def __init__(self, token):
        self.base = f"{const.BASE_URL}{token}/"

    def poll(self, timeout=1200, allowed_types=None):
        lastUpdate = None
        while True:
            if lastUpdate is None:
                response = self.get_updates(offset=-1, timeout=timeout, allowed_types=allowed_types)
            else:
                response = self.get_updates(offset=lastUpdate.getNextUpdateID(), timeout=timeout, allowed_types=allowed_types)

            updates = self.generate_updates(response)

            if updates:
                for item in updates:
                    lastUpdate = item
                    self.process_update(item)

    def add_command(self, command=None, text=None):
        def decorator(func):
            if command is not None:
                self._commands[command] = func
            else:
                if isinstance(text, list):
                    for t in text:
                        self._text[text] = func
                else:
                    self._text[text] = func

        return decorator

    def add_callback(self, callback_data):
        def decorator(func):
            self._callback[callback_data] = func

        return decorator

    def get_updates(self, offset, timeout, allowed_types) -> {}:
        if allowed_types is None:
            allowed_types = [UpdateType.MESSAGE]

        get_update_url = UpdateUrl(self.base) \
            .timeout(timeout) \
            .allowed_updates(allowed_types) \
            .offset(offset, condition=offset is not None) \
            .build()

        response = requests.request("GET", get_update_url, headers={}, data={})
        response = json.loads(response.content)

        return response

    def generate_updates(self, response) -> List[Update]:

        if response.get('ok', False) is True:
            return list(map(lambda update: Update(response=update), response["result"]))
        else:
            raise ValueError(response['error'])

    def process_update(self, item):
        if item.message.text:
            for p in self._text.keys():
                r = re.compile(p)
                if re.fullmatch(r, item.message.text.lower()):
                    self._text.get(p)(item.message)
        if item.getUpdateType() == UpdateType.MESSAGE and item.message.entityType():
            command = item.message.text[item.message.entities[0].offset:item.message.entities[0].length]
            print(command)
            if self._commands.get(command): self._commands.get(command)(item)
        elif item.getUpdateType() == UpdateType.CALLBACK:
            callback = item.callback.message.replyMarkup.keyboards[0].callbackData.split("@")[1]
            self._callback.get(callback)(item)

    def send_message(self, chat_id, text):
        url = self.base + f"sendMessage?chat_id={chat_id}&text={text}"
        requests.request("POST", url, headers={}, data={})

    def send_callback(self, chat_id, text, reply_mark_up):
        url = self.base + f"sendMessage?chat_id={chat_id}&text={text}&reply_markup={reply_mark_up}"
        requests.request("POST", url, headers={}, data={})

    def send_photo(self, chat_id, file):
        up = {'photo': ("i.png", open(file, 'rb'), "multipart/form-data")}
        url = self.base + f"sendPhoto"
        requests.post(url, files=up, data={
            "chat_id": chat_id,
        })


