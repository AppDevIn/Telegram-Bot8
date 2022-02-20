from . import BaseRequest


class MediaRequestBase(BaseRequest):

    def chat_id(self, chat_id):
        self.addParameter("chat_id", chat_id)
        return self

    def caption(self, caption):
        self.addParameter("caption", caption)
        return self

    def parse_mode(self, parse_mode):
        self.addParameter("parse_mode", parse_mode)
        return self

    def caption_entities(self, caption_entities):
        self.addParameter("caption_entities", caption_entities)
        return self

    def disable_notification(self, disable_notification):
        self.addParameter("disable_notification", disable_notification)
        return self

    def protect_content(self, protect_content):
        self.addParameter("protect_content", protect_content)
        return self

    def reply_to_message_id(self, reply_to_message_id):
        self.addParameter("reply_to_message_id", reply_to_message_id)
        return self

    def allow_sending_without_reply(self, allow_sending_without_reply):
        self.addParameter("allow_sending_without_reply", allow_sending_without_reply)
        return self

    def reply_markup(self, reply_markup):
        self.addParameter("reply_markup", reply_markup)
        return self


class PhotoRequest(MediaRequestBase):
    def photo(self, photo):
        self.addParameter("photo", photo)
        return self


class AudioRequest(MediaRequestBase):
    def audio(self, audio):
        self.addParameter("audio", audio)
        return self

    def duration(self, duration):
        self.addParameter("duration", duration)
        return self

    def performer(self, performer):
        self.addParameter("performer", performer)
        return self

    def title(self, title):
        self.addParameter("title", title)
        return self

    def thumb(self, thumb):
        self.addParameter("thumb", thumb)
        return self
