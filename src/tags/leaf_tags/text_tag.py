from abstract_tags.leaf_tag import LeafTag


class TextTag(LeafTag):
    """Represents a special tag that contains only text.
    It is an equivalent of the TextNode in the DOM.
    It allows us to add text and specify its position in the html tree.
    """

    def __init__(self, text: str):
        self.text = text

    def html_string(self, depth=0) -> str:
        """This is a special tag so it implements its own html_string method.
        It doesnt use its class name or attributes, it just returns the text.
        """
        indentation = "  " * depth
        return indentation + self.text

    @property
    def attributes(self):
        """Because this is a special tag, it doesn't have any attributes"""
        return {}
