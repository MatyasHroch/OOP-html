from abstract_tags.leaf_tag import LeafTag


class Input(LeafTag):
    __name = "input"

    def __init__(self, type: str, value=None):
        super().__init__()

        if type is None:
            raise Warning("Input type cannot be None")

        self.type = type
        self.value = value

    @property
    def name(self):
        return Input.__name

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"type": self.type, "value": self.value})
        return attributes
