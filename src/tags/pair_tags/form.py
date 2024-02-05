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
        """Returns the attributes of the tag. It uses the parent attributes and adds the new ones."""

        parent_attributes = super().attributes
        my_attributes = {
            "action": self.action,
            "method": self.method,
            "target": self.target,
            "enctype": self.enctype,
            "novalidate": self.novalidate,
        }

        return {**parent_attributes, **my_attributes}
