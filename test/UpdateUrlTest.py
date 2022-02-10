import unittest

from TelegramBot8 import UpdateUrl


class UpdateUrlTest(unittest.TestCase):

    def setUp(self) -> None:
        self.updateUrl = UpdateUrl("test.com/botnsdjnsj/")

    def test_first_parameter_has_question_mark(self):
        url = self.updateUrl.offset("-1").build()
        split_url = url.split("?")
        assert len(split_url) == 2
        assert split_url[-1] == "offset=-1"

    def test_first_parameter_timeout_has_question_mark(self):
        url = self.updateUrl.timeout("100").build()
        split_url = url.split("?")
        assert len(split_url) == 2
        assert split_url[-1] == "timeout=100"

    def test_url_with_more_then_one_parameter(self):
        url = self.updateUrl\
            .offset("-1")\
            .timeout("100")\
            .allowed_updates([])\
            .build()

        split_url = url.split("?")
        assert len(split_url) == 2
        split_url = split_url[-1].split("&")
        assert len(split_url) == 3
        assert split_url[-1] == "allowed_updates=[]"
        assert split_url[1] == "timeout=100"
        assert split_url[0] == "offset=-1"

    def test_offset_with_condition_being_false(self):
        url = self.updateUrl \
            .offset("-1", condition=False) \
            .build()

        split_url = url.split("?")
        assert len(split_url) == 1
        assert split_url[0] == "test.com/botnsdjnsj/getUpdates"


