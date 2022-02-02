class InlineKeyboard(object):
    keyboards = []

    def __init__(self, response):
        super().__init__()

        for item in response[0]:
            self.keyboards.append(Keyboard(item["regex"], item["callback_data"]))


class Keyboard(object):

    def __init__(self, text, callback_data) -> None:
        super().__init__()
        self.text = text
        self.callbackData = callback_data
