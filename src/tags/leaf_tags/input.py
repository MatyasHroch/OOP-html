from abstract_tags.leaf_tag import LeafTag
from logger import log_warning


class Input(LeafTag):
    """Represents an <input> tag"""

    def __init__(self, type: str):
        """Initializes the <input> tag. If the required attributes are not provided, it logs a warning."""
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
        """Returns the attributes of the tag. It uses the parent attributes and adds the new ones."""

        parent_attributes = super().attributes
        my_attributes = {
            "type": self.type,
            "value": self.value,
            "placeholder": self.placeholder,
            "required": self.required,
            "disabled": self.disabled,
            "readonly": self.readonly,
            "autofocus": self.autofocus,
            "accept": self.accept,
            "autocomplete": self.autocomplete,
        }
        return {**parent_attributes, **my_attributes}
