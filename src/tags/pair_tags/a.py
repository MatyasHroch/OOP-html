from abstract_tags.pair_tag import PairTag
from logger import log_warning


class A(PairTag):
    """Represents an <a> tag"""

    def __init__(self, href: str = None):
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
        attributes = super().attributes
        attributes.update({"href": self.href})
        return attributes
