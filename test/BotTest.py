import unittest

from TelegramBot8 import TeleBot


class BotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = TeleBot("Token")

    def test_generate_updated(self):
        updates = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 452461090,
                    "message": {
                        "message_id": 96,
                        "from": {
                            "id": 645812448,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "chat": {
                            "id": 645812448,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "type": "private"
                        },
                        "date": 1639191220,
                        "regex": "Mm"
                    }
                }
            ]
        })

        assert len(updates) == 1

    def test_generate_updated_throw_value_exception(self):
        self.assertRaises(ValueError, self.bot._generate_updates, {
            "ok": False,
            "error":"Hello error"
        })