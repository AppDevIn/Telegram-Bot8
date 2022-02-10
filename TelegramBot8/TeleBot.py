from typing import List
import re
import requests
import json
import TelegramBot8.Model.Dto.Constants as const
from TelegramBot8 import SetMyCommandRequest, BotCommandScope, BotCommand, CommandRequestBase, \
    bot_commands_from_dict, ForwardRequest, error_from_dict, BaseResponse, ForwardResponse, forward_from_dict, \
    GetMeResponse, get_me_response_from_dict, success_from_dict, UpdateType, Update, UpdateUrl, SendMessageUrl, Commands


class TeleBot:
    _callback = {}
    _text = {}
    _command = Commands()
    headers = {
        'Content-Type': 'application/json'
    }

    def __init__(self, token, limited=None):
        self.base = f"{const.BASE_URL}{token}/"
        self.limited = limited

    def _set_commands(self):

        for command in self._command.get_menu_command_list():
            commands = list(map(lambda x: BotCommand().command(x["command"])
                                .description(x["description"]).build(), command["commands"]))

            if "language_code" in command:
                self.set_my_commands(commands, command["scope"], command["language_code"])
            else:
                self.set_my_commands(commands, command["scope"], None)

    def poll(self, update=None, timeout=1200, allowed_types=None):
        self._set_commands()
        lastUpdate = None
        while True:
            if lastUpdate is None:
                response = self._get_updates(offset=-1, timeout=timeout, allowed_types=allowed_types)
            else:
                response = self._get_updates(offset=lastUpdate.getNextUpdateID(), timeout=timeout,
                                             allowed_types=allowed_types)

            updates = self._generate_updates(response)

            if updates:
                for item in updates:
                    lastUpdate = item
                    self._process_update(item)
                    if update is not None:
                        update(item)

    def _generate_updates(self, response) -> List[Update]:

        if response.get('ok', False) is True:
            return list(map(lambda update: Update(response=update), response["result"]))
        else:
            raise ValueError(response['error'])

    def add_regex_helper(self, regex):
        """Method to look at each chat and if the message matches it will triggers

        :param regex: The regex pattern you want the text to match
        """

        def decorator(func):
            if isinstance(regex, list):
                for t in regex:
                    self._text[t] = func
            else:
                self._text[regex] = func

        return decorator

    def add_command_helper(self, command):
        """This method allows you handle commands send from telegram

        :param command: Add the command you want to handle e.g. /hello_world
        """

        def decorator(func):
            if command is None: return

            if isinstance(command, list):
                for c in command:
                    self._command.add_command(c, func)
            else:
                self._command.add_command(command, func)

        return decorator

    def add_command_menu_helper(self, command, scope=BotCommandScope.BotCommandScopeDefault()[0], description="",
                                language=None):
        """This method allows you handle commands send from telegram and allows you to add the \
        command to telegram menu

        :param command: Add the command you want to handle e.g. /hello_world
        :param scope: Use BotCommandScope to view the different scopes. A JSON-serialized object, \
        describing scope of users for which the commands are relevant.
        :param description: Description of the command
        :param language: A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from \
        the given scope, for whose language there are no dedicated commands

        :return: Error or success messages
        """

        def decorator(func):
            if command is None: return

            if isinstance(command, list):
                for c in command:
                    self._command.add_command(c, func)
                self._command.add_command_menu(command[0], func, description, scope, language)
            else:
                self._command.add_command(command, func)
                self._command.add_command_menu(command, func, description, scope, language)

        return decorator

    def add_callback(self, callback_data):
        """Method yet to be implemented

        :param callback_data:
        :return:
        """

        def decorator(func):
            self._callback[callback_data] = func

        return decorator

    def _get_updates(self, offset, timeout, allowed_types) -> {}:
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

    def _process_update(self, item):
        if len(item.message.entities) != 0 and item.message.entities[0].type == "bot_command" and \
                item.getUpdateType() == UpdateType.MESSAGE and item.message.entityType():
            command = item.message.text[item.message.entities[0].offset:item.message.entities[0].length]
            if self._command.has_command(command): self._command.get_command(command)(item.message)
        elif item.message.text:
            for p in self._text.keys():
                r = re.compile(p)
                if re.fullmatch(r, item.message.text.lower()):
                    self._text.get(p)(item.message)
        elif item.getUpdateType() == UpdateType.CALLBACK:
            callback = item.callback.message.replyMarkup.keyboards[0].callbackData.split("@")[1]
            self._callback.get(callback)(item.message)
        else:
            print("DEAD ☠️")

    def get_me(self) -> GetMeResponse:
        """Get's information about the bot

        :return: Returns information about the bot using the GetMeResponse class
        """
        url = f'{self.base}getMe'
        response = requests.post(url, headers={}, data={})
        return get_me_response_from_dict(response.text)

    def send_message(self, chat_id, text, parse_mode=None, disable_web_page_preview=None,
                     disable_notification=None, reply_to_message_id=None,
                     allow_sending_without_reply=None, reply_markup=None):
        """To send message to telegram using this method

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :param text: Text of the message to be sent, 1-4096 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the message text allowing for bold and italic formats
        :param disable_web_page_preview: Disables link previews for links in this message
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup: Pass True, if the message should be sent even if the specified replied-to message is not found
        """
        sendMessageUrl = SendMessageUrl(self.base).text(text).chat_id(chat_id).parse_mode(parse_mode) \
            .disable_web_page_preview(disable_web_page_preview) \
            .disable_notification(disable_notification) \
            .reply_to_message_id(reply_to_message_id) \
            .allow_sending_without_reply(allow_sending_without_reply) \
            .reply_markup(reply_markup).build()
        requests.request("POST", sendMessageUrl, headers={}, data={})

    def forward_messaged(self, chat_id, from_chat_id, message_id: int,
                         disable_notification: bool = None, protect_content: bool = None) -> ForwardResponse:
        """Use this method to forward messages of any kind. Service messages can't be forwarded.
         On success, the sent Message is returned.


         :param chat_id: Unique identifier for the target chat or username of the target channel
         :param from_chat_id: Unique identifier for the chat group where the original message was sent
         :param message_id: Message id in the chat group specified in from_chat_id
         :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
         :param protect_content: Protects the contents of the forwarded message from forwarding and saving

         :return: ForwardResponse containing the message
        """
        url = f'{self.base}forwardMessage'
        request_body = ForwardRequest()
        request_body = request_body.chat_id(chat_id).from_chat_id(from_chat_id).message_id(message_id). \
            disable_notification(disable_notification).protect_content(protect_content).build()

        response = requests.post(url, headers={}, data=request_body)
        return forward_from_dict(response.text)

    def set_my_commands(self, commands: [BotCommand], scope: {} = None, language_code: str = None) -> BaseResponse:
        """This allows you to set a list of commands in the page where your bot will exist

        :param commands: Is an array of CommandDto. At most 100 commands can be specified.
        :param scope: A JSON-serialized object, describing scope of users for which the commands are relevant.Defaults \
        to BotCommandScopeDefault. You can use the BotCommandScope to get values in
        :param language_code: A two-letter ISO 639-1 language code. If empty, commands will be applied to all users \
        from the given scope, for whose language there are no dedicated commands.

        :return: Error or success messages
        """

        url = f'{self.base}setMyCommands'
        request_body = SetMyCommandRequest().commands(commands).scope(scope) \
            .language_code(language_code).build()

        payload = json.dumps(request_body)
        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code != 200:
            return error_from_dict(response.text).status_code(response.status_code)
        else:
            return success_from_dict(response.text)

    def get_my_commands(self, scope: {} = None, language_code: str = None):
        """Use this method to get the current list of the bot's commands for the given scope and user language.

        :param scope: A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code or an empty string

        :return: Array of BotCommand on success. If commands aren't set, an empty list is returned.
        """

        url = f'{self.base}getMyCommands'
        request_body = CommandRequestBase().scope(scope) \
            .language_code(language_code).build()

        payload = json.dumps(request_body)
        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code != 200:
            return error_from_dict(response.text).status_code(response.status_code)
        else:
            return bot_commands_from_dict(response.text)

    def delete_my_commands(self, scope: {} = None, language_code: str = None) -> BaseResponse:
        """Use this method to delete the list of the bot's commands for the given scope and user language. \
        After deletion, higher level commands will be shown to affected users.

        :param scope: A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault.
        :param language_code: A two-letter ISO 639-1 language code or an empty string

        :return: True on success
        """

        url = f'{self.base}deleteMyCommands'
        request_body = CommandRequestBase().scope(scope) \
            .language_code(language_code).build()

        payload = json.dumps(request_body)
        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code != 200:
            return error_from_dict(response.text).status_code(response.status_code)
        else:
            return success_from_dict(response.text)

    def send_photo(self, chat_id, file):
        """ Method send image to a specfic chat

        :param chat_id: Unique identifier for the target chat or username of the target channel
        :param file: The file which the whole belong to
        :return:
        """
        up = {'photo': ("i.png", open(file, 'rb'), "multipart/form-data")}
        url = self.base + f"sendPhoto"
        requests.post(url, files=up, data={
            "chat_id": chat_id,
        })
