from abstract_tags.pair_tag import PairTag


class Form(PairTag):
    __name = "form"

    def __init__(self):
        super().__init__()
        self.action = None
        self.method = None

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        self._method = method
