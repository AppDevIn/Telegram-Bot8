import unittest
from typing import List

from TelegramBot8 import TeleBot, UpdateList, Update, Message


class BotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = TeleBot("Token")

    def test_generate_updated_for_test(self):
        updates = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 1,
                    "message": {
                        "message_id": 96,
                        "from": {
                            "id": 3,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "chat": {
                            "id": 200,
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
                    "update_id": 1,
                    "message": {
                        "message_id": 310,
                        "from": {
                            "id": 3,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "chat": {
                            "id": 200,
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
                    "update_id": 1,
                    "message": {
                        "message_id": 311,
                        "from": {
                            "id": 3,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "chat": {
                            "id": 200,
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
                    "update_id": 1,
                    "message": {
                        "message_id": 330,
                        "from": {
                            "id": 3,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "chat": {
                            "id": 200,
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

    def test_check_if_the_update_id_is_correct(self):
        updates = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 1,
                    "message": {
                        "message_id": 1,
                        "from": {
                            "id": 3,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "chat": {
                            "id": 200,
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

    def test_check_if_able_to_process_group_update(self):
        updates = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 1,
                    "message": {
                        "message_id": 222,
                        "from": {
                            "id": 2343,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "chat": {
                            "id": 4323423,
                            "title": "Eth Bot",
                            "type": "group",
                            "all_members_are_administrators": True
                        },
                        "date": 1644938471,
                        "text": "/hello@SliverFridayDevBot",
                        "entities": [
                            {
                                "offset": 0,
                                "length": 25,
                                "type": "bot_command"
                            }
                        ]
                    }
                }
            ]
        })
        assert len(updates) == 1

    def test_when_unknown_field_exist_is_it_able_to_process(self):
        updates: List[Update] = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 1,
                    "message": {
                        "message_id": 222,
                        "from": {
                            "id": 2343,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "Unknown": "HAHAHHAHA",
                        "chat": {
                            "id": 32443232,
                            "title": "Eth Bot",
                            "type": "group",
                            "all_members_are_administrators": True
                        },
                        "date": 1644938471,
                        "text": "/hello@SliverFridayDevBot",
                        "entities": [
                            {
                                "offset": 0,
                                "length": 25,
                                "type": "bot_command"
                            }
                        ]
                    }
                }
            ]
        })

        assert updates[0].to_dict().get("message").get("Unknown") == "HAHAHHAHA"
        assert len(updates) == 1

    def test_when_user_listen_command_update_response_to_the_method(self):
        updates: List[Update] = self.bot._generate_updates({
            "ok": True,
            "result": [
                {
                    "update_id": 34432,
                    "message": {
                        "message_id": 370,
                        "from": {
                            "id": 234324,
                            "is_bot": False,
                            "first_name": "Jeya",
                            "username": "jrjeya",
                            "language_code": "en"
                        },
                        "chat": {
                            "id": -3243232423,
                            "title": "Eth Bot",
                            "type": "group",
                            "all_members_are_administrators": True
                        },
                        "date": 1644942692,
                        "text": "/group@SliverFridayDevBot",
                        "entities": [
                            {
                                "offset": 0,
                                "length": 25,
                                "type": "bot_command"
                            }
                        ]
                    }
                }
            ]
        })
        self.bot._command.add_command("/group", lambda message: message)
        assert self.bot._process_update(updates[0])

    def test_generate_updated_throw_value_exception(self):
        self.assertRaises(ValueError, self.bot._generate_updates, {
            "ok": False,
            "error": "Hello error"
        })
