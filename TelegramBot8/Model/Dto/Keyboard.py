from ..Reqest import BaseRequest


# TODO: Add login_url and callback_game
class InlineKeyboard(BaseRequest):

    def text(self, text):
        self.addParameter("text", text)
        return self

    def url(self, url):
        self.addParameter("url", url)
        return self

    def callback_data(self, callback_data):
        self.addParameter("callback_data", callback_data)
        return self

    def switch_inline_query(self, switch_inline_query):
        self.addParameter("switch_inline_query", switch_inline_query)
        return self

    def switch_inline_query_current_chat(self, switch_inline_query_current_chat):
        self.addParameter("switch_inline_query_current_chat", switch_inline_query_current_chat)
        return self

    def pay(self, pay):
        self.addParameter("pay", pay)
        return self
