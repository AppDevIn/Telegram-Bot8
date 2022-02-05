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


class BotCommandScope(Enum):
    BotCommandScopeDefault = {"type": "default"},
    BotCommandScopeAllPrivateChats = {"type": "all_private_chats"},
    BotCommandScopeAllGroupChats = {"type": "all_group_chats"},
    BotCommandScopeAllChatAdministrators = {"type": "all_chat_administrators"},
    BotCommandScopeChat = lambda chat_id: {"type": "chat", "chat_id": chat_id},
    BotCommandScopeChatAdministrators = lambda chat_id: {"type": "chat_administrators", "chat_id": chat_id},
    BotCommandScopeChatMember = lambda chat_id: {"type": "chat_member", "chat_id": chat_id},
