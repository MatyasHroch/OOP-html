from abstract_tags.pair_tag import PairTag
from logger import log_warning


class A(PairTag):
    """Represents an <a> tag"""

    def __init__(self, href: str = None):
        """Initializes the <a> tag. If the required attributes are not provided, it logs a warning."""
        super().__init__()

        if href is None:
            log_warning("Href is required for <a> tag")

        # Required attributes
        self.href = href

        # Optional attributes
        self.target: str = None
        self.download: str = None
        self.rel: str = None
        self.type: str = None
        self.hreflang: str = None
        self.referrerpolicy: str = None

    @property
    def attributes(self):
        """Returns the attributes of the tag. It uses the parent attributes and adds the new ones."""

        parent_attributes = super().attributes
        my_attributes = {
            "href": self.href,
            "target": self.target,
            "download": self.download,
            "rel": self.rel,
            "type": self.type,
            "hreflang": self.hreflang,
            "referrerpolicy": self.referrerpolicy,
        }
        return {**parent_attributes, **my_attributes}
