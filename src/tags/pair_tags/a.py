from abstract_tags.pair_tag import PairTag


class A(PairTag):
    __name = "a"

    def __init__(self, href: str = None):
        super().__init__()

        if href is None:
            raise Warning("Href cannot be None")

        self._href = href

    @property
    def name(self):
        return A.__name

    @property
    def attributes(self):
        attributes = super().attributes
        attributes.update({"href": self._href})
        return attributes
