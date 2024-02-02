from abstract_tags.pair_tag import PairTag
from logger import log_warning


class A(PairTag):
    """Represents an <a> tag"""

    # __name = "a"

    def __init__(self, href: str = None):
        super().__init__()

        if href is None:
            log_warning("Href is required for <a> tag")

        self._href = href

    # @property
    # def name(self):
    #     return A.__name

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"href": self._href})
        return attributes
