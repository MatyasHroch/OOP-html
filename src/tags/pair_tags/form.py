from abstract_tags.pair_tag import PairTag


class FormMethod:
    GET = "get"
    POST = "post"


class Form(PairTag):
    """Represents a <form> tag"""

    def __init__(self):
        super().__init__()

        # optional attributes
        self.action = None
        self.method = None
        self.action = None
        self.method = None
        self.target = None
        self.enctype = None
        self.novalidate = None

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"action": self.action, "method": self.method})
        return attributes
