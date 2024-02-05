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
        """Returns the attributes of the tag. It uses the parent attributes and adds the new ones."""

        parent_attributes = super().attributes
        my_attributes = {
            "size": self.size,
            "multiple": self.multiple,
            "disabled": self.disabled,
            "autofocus": self.autofocus,
            "required": self.required,
        }

        return {**parent_attributes, **my_attributes}
