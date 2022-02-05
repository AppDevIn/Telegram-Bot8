from model.Reqest.Base import BaseRequest


class CommandRequestBase(BaseRequest):

    def language_code(self, language_code):
        self.addParameter("language_code", language_code)
        return self

    def scope(self, scope):
        self.addParameter("scope", scope)
        return self


class SetCommandRequest(CommandRequestBase):
    def commands(self, commands):
        self.addParameter("commands", commands)
        return self
