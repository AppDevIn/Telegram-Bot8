from . import BaseRequest


class MessageRequest(BaseRequest):

    def chat_id(self, chat_id):
        self.addParameter("chat_id", chat_id)
        return self

    def disable_notification(self, disable_notification):
        self.addParameter("disable_notification", disable_notification)
        return self

    def protect_content(self, protect_content):
        self.addParameter("protect_content", protect_content)
        return self
