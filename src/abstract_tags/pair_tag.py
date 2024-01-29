from abc import ABC, abstractmethod, abstractproperty

from abstract_tags.tag import Tag


class PairTag(Tag):
    def __init__(self, children: list[Tag] = None) -> None:
        super().__init__()
        self.children = children

    def __add__(self, other: "Tag"):
        self.append_child(other)

    @abstractmethod
    def append_child(self, other: "Tag"):
        pass

    @abstractproperty
    def children(self) -> list["Tag"]:
        pass

    def html_string(self, include_children=True) -> str:
        children_html = ""
        if include_children:
            # children_html = "\n\t"
            for child in self.children:
                children_html += child.html_string()

        return f"<{self.name}>{children_html}<{self.name}/>\n"
