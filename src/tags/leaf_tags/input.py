from abstract_tags.leaf_tag import LeafTag
from logger import log_warning


class Input(LeafTag):
    """Represents an <input> tag"""

    def __init__(self, type: str):
        super().__init__()

        if type is None:
            log_warning("Type is required for <input> tag")

        # Required attributes
        self.type = type

        # Optional attributes
        self.value: any = None
        self.placeholder: str = None
        self.required: bool = None
        self.disabled: bool = None
        self.readonly: bool = None
        self.autofocus: bool = None
        self.accept: str = None
        self.autocomplete: str = None

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"type": self.type, "value": self.value})
        return attributes
