class UrlBuilder:
    def __init__(self, base):
        self.base = base
        self.firstParameter = True

    def addParameter(self, value) -> str:
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
