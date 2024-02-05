from abstract_tags.pair_tag import PairTag


class Div(PairTag):
    """Represents a <div> tag"""

    def __init__(self):
        super().__init__()

    @property
    def attributes(self):
        """No special attributes for the div tag. It just returns the parent attributes."""
        return super().attributes
