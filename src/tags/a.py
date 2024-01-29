from abstract_tags.leaf_tag import LeafTag


class A(LeafTag):
    __name = "a"

    def __init__(self):
        super().__init__()
        self._href = None

    @property
    def name(self):
        return A.__name

    @property
    def href(self):
        return self._href

    @href.setter
    def href(self, href):
        self._href = href
