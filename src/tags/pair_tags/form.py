from abstract_tags.pair_tag import PairTag


class Form(PairTag):
    """Represents a <form> tag"""

    __name = "form"

    def __init__(self):
        super().__init__()

        self.action = None
        self.method = None

    @property
    def name(self):
        return Form.__name

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"action": self.action, "method": self.method})
        return attributes
