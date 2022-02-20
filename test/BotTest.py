import json
import unittest
from typing import List

from TelegramBot8 import TeleBot, UpdateList, Update, Message, photo_response_from_dict


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

    def test_when_user_return_response_of_send_photo(self):
        response = photo_response_from_dict(json.dumps({
            "ok": True,
            "result": {
                "message_id": 321,
                "from": {
                    "id": 312,
                    "is_bot": True,
                    "first_name": "fds",
                    "username": "fds"
                },
                "chat": {
                    "id": 321,
                    "first_name": "dsf",
                    "username": "dfs",
                    "type": "private"
                },
                "date": 1645329122,
                "photo": [
                    {
                        "file_id": "AgACAgQAAxkDAAIBfGIRuuIROH8vPzQgHNFip1tVQplHAAL0rDEblFq8UWL51XJ0ofQnAQADAgADcwADIwQ",
                        "file_unique_id": "AQAD9KwxG5RavFF4",
                        "file_size": 1702,
                        "width": 90,
                        "height": 67
                    },
                    {
                        "file_id": "AgACAgQAAxkDAAIBfGIRuuIROH8vPzQgHNFip1tVQplHAAL0rDEblFq8UWL51XJ0ofQnAQADAgADbQADIwQ",
                        "file_unique_id": "AQAD9KwxG5RavFFy",
                        "file_size": 21334,
                        "width": 320,
                        "height": 240
                    },
                    {
                        "file_id": "AgACAgQAAxkDAAIBfGIRuuIROH8vPzQgHNFip1tVQplHAAL0rDEblFq8UWL51XJ0ofQnAQADAgADeAADIwQ",
                        "file_unique_id": "AQAD9KwxG5RavFF9",
                        "file_size": 95744,
                        "width": 800,
                        "height": 600
                    },
                    {
                        "file_id": "AgACAgQAAxkDAAIBfGIRuuIROH8vPzQgHNFip1tVQplHAAL0rDEblFq8UWL51XJ0ofQnAQADAgADeQADIwQ",
                        "file_unique_id": "AQAD9KwxG5RavFF-",
                        "file_size": 165097,
                        "width": 1200,
                        "height": 900
                    }
                ]
            }
        }))

        assert len(response.result.photo) == 4

    def test_when_user_return_response_of_send_audio(self):
        response = photo_response_from_dict(json.dumps({
            "ok": True,
            "result": {
                "message_id": 21321,
                "from": {
                    "id": 23121,
                    "is_bot": True,
                    "first_name": "dcds",
                    "username": "dfsfdsdfs"
                },
                "chat": {
                    "id": 3234134,
                    "first_name": "sdfdfs",
                    "username": "dsfdfs",
                    "type": "private"
                },
                "date": 1645336772,
                "audio": {
                    "duration": 372,
                    "file_name": "SoundHelix-Song-1.mp3",
                    "mime_type": "audio/mpeg",
                    "performer": "SoundHelix",
                    "file_id": "CQACAgQAAxkDAAIBoWIR2MQFHxzs9C0hb9W9ExOtVc-7AAL_AQAC80lEU2zGX4cFNifOIwQ",
                    "file_unique_id": "AgAD_wEAAvNJRFM",
                    "file_size": 8945229
                }
            }
        }))

        assert response.to_dict()["result"]["audio"]["file_name"] == "SoundHelix-Song-1.mp3"

    def test_generate_updated_throw_value_exception(self):
        self.assertRaises(ValueError, self.bot._generate_updates, {
            "ok": False,
            "error": "Hello error"
        })
