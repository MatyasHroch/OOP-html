from abstract_tags.leaf_tag import LeafTag


class Input(LeafTag):
    __name = "input"

    def __init__(self):
        super().__init__()
        self.type = None
        self.value = None

    @property
    def name(self):
        return Input.__name
