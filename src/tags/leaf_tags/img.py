from enum import Enum

from abstract_tags.leaf_tag import LeafTag
from logger import log_warning


# we can use the Enum class to be more concrete about attribute values
class Loading(Enum):
    EAGER = "eager"
    LAZY = "lazy"
    AUTO = "auto"


class Img(LeafTag):
    """Represents an <img> tag"""

    def __init__(self, src: str, alt: str = None):
        """Initializes the <img> tag. If the required attributes are not provided, it logs a warning."""
        super().__init__()

        if src is None:
            log_warning("Src is required for <img> tag")

        if alt is None:
            log_warning("Alt is required in the <img> tag for a validation")

        # Required attributes
        self.src = src
        self.alt = alt

        # Optional attributes
        self.width: float = None
        self.height: float = None
        self.loading: str = None
        self.decoding: str = None
        self.crossorigin: str = None
        self.usemap: str = None
        self.ismap: bool = None
        self.loading: Loading = None

    @property
    def attributes(self):
        """Returns the attributes of the tag. It uses the parent attributes and adds the new ones."""

        parent_attributes = super().attributes
        my_attributes = {
            "src": self.src,
            "alt": self.alt,
            "width": self.width,
            "height": self.height,
            "loading": self.loading,
            "decoding": self.decoding,
            "crossorigin": self.crossorigin,
            "usemap": self.usemap,
            "ismap": self.ismap,
        }
        return {**parent_attributes, **my_attributes}

    # EXAMPLE OF HOW TO CHANGE THE PRINTED NAME OF THE TAG
    # If we want to print other name for the tag than the class name
    # we can just override the name property:
    # @property
    # def name(self):
    #     return "img"
