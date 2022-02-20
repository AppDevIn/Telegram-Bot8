from . import BaseRequest
from ... import ParseMode


class UpdateRequest(BaseRequest):

    def timeout(self, timeout):
        self.addParameter("timeout", timeout)
        return self

    def offset(self, offset, condition=True):
        if condition:
            self.addParameter("offset", offset)
        return self

    def allowed_updates(self, allowed_updates: []):
        self.addParameter("allowed_updates", allowed_updates)
        return self

    def limit(self, limit: int):
        self.addParameter("limit", limit)
        return self


class SendMessageRequest(BaseRequest):

    def text(self, text):
        self.addParameter("text", text)
        return self

    def chat_id(self, chat_id):
        self.addParameter("chat_id", chat_id)
        return self

    def parse_mode(self, parse_mode: ParseMode):
        if parse_mode is not None:
            parse_mode = parse_mode.value
        self.addParameter("parse_mode", parse_mode)
        return self

    def disable_web_page_preview(self, disable_web_page_preview):
        self.addParameter("disable_web_page_preview", disable_web_page_preview)
        return self

    def disable_notification(self, disable_notification):
        self.addParameter("disable_notification", disable_notification)
        return self

    def reply_to_message_id(self, reply_to_message_id):
        self.addParameter("reply_to_message_id", reply_to_message_id)
        return self

    def allow_sending_without_reply(self, allow_sending_without_reply):
        self.addParameter("allow_sending_without_reply", allow_sending_without_reply)
        return self

    def reply_markup(self, reply_markup):
        self.addParameter("reply_markup", reply_markup)
        return self
