from abstract_tags.pair_tag import PairTag


class Form(PairTag):
    """Represents a <form> tag"""

    def __init__(self):
        super().__init__()

        self.action = None
        self.method = None

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"action": self.action, "method": self.method})
        return attributes
