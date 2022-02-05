import json
from enum import Enum

from model.Reqest.Base import BaseRequest


class CommandRequestBase(BaseRequest):

    def language_code(self, language_code):
        self.addParameter("language_code", language_code)
        return self

    def scope(self, scope):
        self.addParameter("scope", scope)
        return self


class CommandDto(BaseRequest):
    def command(self, command):
        self.addParameter("command", command)
        return self

    def description(self, description):
        self.addParameter("description", description)
        return self


class SetCommandRequest(CommandRequestBase):

    def commands(self, command: [CommandDto]):
        self.addParameter("commands", command)
        return self


class BotCommandScope:

    @staticmethod
    def BotCommandScopeDefault():
        return {"type": "default"},

    @staticmethod
    def BotCommandScopeAllPrivateChats():
        return {"type": "all_private_chats"},

    @staticmethod
    def BotCommandScopeAllGroupChats():
        return {"type": "all_group_chats"},

    @staticmethod
    def BotCommandScopeAllChatAdministrators():
        return {"type": "all_chat_administrators"},

    @staticmethod
    def BotCommandScopeChat(chat_id):
        return {"type": "chat", "chat_id": chat_id}

    @staticmethod
    def BotCommandScopeChatAdministrators(chat_id):
        return {"type": "chat_administrators", "chat_id": chat_id}

    @staticmethod
    def BotCommandScopeChatMember(chat_id, user_id):
        return {"type": "chat_member", "chat_id": chat_id, "user_id": user_id}
