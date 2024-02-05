from abstract_tags.tag import Tag
from abstract_tags.pair_tag import PairTag


class LeafTag(Tag):
    """Represents a tag that does not have any children.
    It is an abstract class, so it should not be created directly.
    The main purpose of this class is to implement html_string method for all the leaf tags.
    """

    def __init__(self):
        super().__init__()

    @property
    def parent(self) -> PairTag:
        """This class specifies the parent property as a PairTag."""
        return self._parent

    @property
    def attributes(self) -> dict[str, str]:
        return super().attributes

    def html_string(self, include_children=True, depth=0) -> str:
        """Returns the html string representation of all common leaf tags."""

        indentation = "  " * depth
        attributes_str = ""

        if self.attributes:
            attributes_str = f" {self.attributes_str}"

        return f"{indentation}<{self.name}{attributes_str}/>"
