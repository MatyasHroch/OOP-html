from abstract_tags.pair_tag import PairTag


class Select(PairTag):
    """Represents a <select> tag"""

    __name = "select"

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return Select.__name

    @property
    def attributes(self):
        return super().attributes
