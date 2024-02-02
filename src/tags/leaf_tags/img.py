from abstract_tags.leaf_tag import LeafTag


class Img(LeafTag):
    """Represents an <img> tag"""

    # __name = "img"

    def __init__(self, src: str, alt: str = None):
        super().__init__()

        if src is None:
            raise Warning("Src is required")

        if alt is None:
            raise Warning("Alt is required for accessibility and validation")

        self.src = src
        self.alt = alt

    # @property
    # def name(self):
    #     return Img.__name

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"src": self.src, "alt": self.alt})
        return attributes
