import pdb
from typing import List
import re
import requests
import json
import model.Constants as const
from url.UrlBuilder import SendMessageUrl, UpdateUrl

from model.Update import UpdateType, Update


class TeleBot:
    _commands = {}
    _callback = {}
    _text = {}

    def __init__(self, token, limited=None):
        self.base = f"{const.BASE_URL}{token}/"
        self.limited = limited

    def poll(self, update=None, timeout=1200, allowed_types=None):
        lastUpdate = None
        while True:
            if lastUpdate is None:
                response = self.get_updates(offset=None, timeout=timeout, allowed_types=allowed_types)
            else:
                response = self.get_updates(offset=lastUpdate.getNextUpdateID(), timeout=timeout,
                                            allowed_types=allowed_types)

            updates = self.generate_updates(response)

            if updates:
                for item in updates:
                    lastUpdate = item
                    self.process_update(item)
                    if update is not None:
                        update(item)

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
        if item.message.fromUser.getID() != int(self.limited):
            return
        if len(item.message.entities) != 0 and item.message.entities[0].type == "bot_command" and item.getUpdateType() == UpdateType.MESSAGE and item.message.entityType():
            command = item.message.text[item.message.entities[0].offset:item.message.entities[0].length]
            if self._commands.get(command): self._commands.get(command)(item.message)
        elif item.message.text:
            for p in self._text.keys():
                r = re.compile(p)
                if re.fullmatch(r, item.message.text.lower()):
                    self._text.get(p)(item.message)
        elif item.getUpdateType() == UpdateType.CALLBACK:
            callback = item.callback.message.replyMarkup.keyboards[0].callbackData.split("@")[1]
            self._callback.get(callback)(item.message)

    def send_message(self, chat_id, text, parse_mode=None, disable_web_page_preview=None,
                     disable_notification=None, reply_to_message_id=None,
                     allow_sending_without_reply=None, reply_markup=None):
        sendMessageUrl = SendMessageUrl(self.base).text(text).chat_id(chat_id).parse_mode(parse_mode) \
            .disable_web_page_preview(disable_web_page_preview) \
            .disable_notification(disable_notification) \
            .reply_to_message_id(reply_to_message_id) \
            .allow_sending_without_reply(allow_sending_without_reply) \
            .reply_markup(reply_markup).build()
        requests.request("POST", sendMessageUrl, headers={}, data={})

    def send_photo(self, chat_id, file):
        up = {'photo': ("i.png", open(file, 'rb'), "multipart/form-data")}
        url = self.base + f"sendPhoto"
        requests.post(url, files=up, data={
            "chat_id": chat_id,
        })
