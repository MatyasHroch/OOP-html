from abstract_tags.pair_tag import PairTag


class Select(PairTag):
    __name = "select"

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return Select.__name
