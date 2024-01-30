from abstract_tags.pair_tag import PairTag


class Form(PairTag):
    __name = "form"

    def __init__(self):
        super().__init__()
        self.action = None
        self.method = None

    @property
    def name(self):
        return Form.__name
