import unittest

from TelegramBot8 import TeleBot


class BotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = TeleBot("Token")

    def test_generate_updated_for_test(self):
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
                        "text": "Mm"
                    }
                }
            ]
        })
        assert len(updates) == 1

    def test_generate_updated_for_command(self):
        updates = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 221364578,
                    "message": {
                        "message_id": 310,
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
                        "date": 1644754404,
                        "text": "/hello",
                        "entities": [
                            {
                                "offset": 0,
                                "length": 6,
                                "type": "bot_command"
                            }
                        ]
                    }
                },
                {
                    "update_id": 221364579,
                    "message": {
                        "message_id": 311,
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
                        "date": 1644754415,
                        "text": "Ggg"
                    }
                }
            ]
        })
        assert len(updates) == 2

    def test_generate_updated_for_a_list_of_result(self):
        updates = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 221364591,
                    "message": {
                        "message_id": 330,
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
                        "date": 1644761500,
                        "text": "/hello",
                        "entities": [
                            {
                                "offset": 0,
                                "length": 6,
                                "type": "bot_command"
                            }
                        ]
                    }
                }
            ]
        })
        assert len(updates) == 1

    def check_if_the_update_id_is_correct(self):
        updates = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 221364591,
                    "message": {
                        "message_id": 1,
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
                        "date": 1644761500,
                        "text": "/hello",
                        "entities": [
                            {
                                "offset": 0,
                                "length": 6,
                                "type": "bot_command"
                            }
                        ]
                    }
                }
            ]
        })
        assert updates[0].getNextUpdateID() == 2

    def test_generate_updated_throw_value_exception(self):
        self.assertRaises(ValueError, self.bot._generate_updates, {
            "ok": False,
            "error":"Hello error"
        })