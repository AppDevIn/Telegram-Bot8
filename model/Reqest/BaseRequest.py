import json


class BaseSendRequest(object):

    body = {}

    def chat_id(self, chat_id):
        self.addParameter("chat_id", chat_id)
        return self

    def disable_web_page_preview(self, disable_web_page_preview):
        self.addParameter("disable_web_page_preview", disable_web_page_preview)
        return self

    def protect_content(self, protect_content):
        self.addParameter("protect_content", protect_content)
        return self

    def addParameter(self, key, value, not_required=False) -> {}:
        if not_required or "None" in value:
            return self.body
        self.body[key] = value
        return self.body

    def build(self) -> {}:
        return self.body
