from abstract_tags.leaf_tag import LeafTag


class Img(LeafTag):
    __name = "img"

    def __init__(self):
        super().__init__()
        self.src = None
        self.alt = None

    # TODO TODO TODO try it with '@property' in the grand parent class
    @property
    def name(self):
        return Img.__name
