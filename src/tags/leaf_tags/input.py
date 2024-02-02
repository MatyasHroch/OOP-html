from abstract_tags.leaf_tag import LeafTag
from logger import log_warning


class Input(LeafTag):
    """Represents an <input> tag"""

    def __init__(self, type: str, value=None):
        super().__init__()

        if type is None:
            log_warning("Type is required for <input> tag")

        self.type = type
        self.value = value

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"type": self.type, "value": self.value})
        return attributes
