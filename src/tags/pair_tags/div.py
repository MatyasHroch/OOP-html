from abstract_tags.pair_tag import PairTag


class Div(PairTag):
    __name = "div"

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return Div.__name

    @property
    def attributes(self):
        return super().attributes
