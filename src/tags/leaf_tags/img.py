from abstract_tags.leaf_tag import LeafTag
from logger import log_warning


class Img(LeafTag):
    """Represents an <img> tag"""

    def __init__(self, src: str, alt: str = None):
        super().__init__()

        if src is None:
            log_warning("Src is required for <img> tag")

        if alt is None:
            log_warning(
                "Alt is required in the <img> tag for accessibility and validation"
            )

        self.src = src
        self.alt = alt

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"src": self.src, "alt": self.alt})
        return attributes
