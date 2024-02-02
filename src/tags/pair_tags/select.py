from abstract_tags.pair_tag import PairTag


class Select(PairTag):
    """Represents a <select> tag"""

    def __init__(self):
        super().__init__()

        # Optional attributes
        self.size = None
        self.multiple = None
        self.disabled = None
        self.autofocus = None
        self.required = None

    @property
    def attributes(self):
        return super().attributes
