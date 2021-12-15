class UrlBuilder:
    def __init__(self, base):
        self.base = base
        self.firstParameter = True

    def addParameter(self, value, condition=False) -> str:
        if condition or "None" in value:
            return self.base
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


class SendMessageUrl(UrlBuilder):

    def __init__(self, url):
        self.base = url + "sendMessage"
        super(SendMessageUrl, self).__init__(self.base)

    def text(self, text):
        self.addParameter(f"text={text}")
        return self

    def chat_id(self, chat_id):
        self.addParameter(f"chat_id={chat_id}")
        return self

    def parse_mode(self, parse_mode):
        self.addParameter(f"parse_mode={parse_mode}")
        return self

    def disable_web_page_preview(self, disable_web_page_preview):
        self.addParameter(f"disable_web_page_preview={disable_web_page_preview}")
        return self

    def disable_notification(self, disable_notification):
        self.addParameter(f"disable_notification={disable_notification}")
        return self

    def reply_to_message_id(self, reply_to_message_id):
        self.addParameter(f"reply_to_message_id={reply_to_message_id}")
        return self

    def allow_sending_without_reply(self, allow_sending_without_reply):
        self.addParameter(f"allow_sending_without_reply={allow_sending_without_reply}")
        return self

    def reply_markup(self, reply_markup):
        self.addParameter(f"reply_markup={reply_markup}")
        return self

