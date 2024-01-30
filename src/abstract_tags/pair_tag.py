from abc import ABC, abstractmethod, abstractproperty

from abstract_tags.tag import Tag


class PairTag(Tag):
    def __init__(self, children: list[Tag] = []) -> None:
        super().__init__()  # it will create __parent and __classes attributes
        if children:
            self.__children = children

    def __add__(self, other: "Tag"):
        self.append_child(other)

    def append_child(self, other: "Tag"):
        self.__children.append(other)
        other.__parent = self

    @property
    def parent(self) -> "PairTag":
        return self.__parent

    @property
    def children(self) -> list["Tag"]:
        return self.__children

    @children.setter
    def children(self, children: list["Tag"]):
        pass

    def html_string(self, include_children=True) -> str:
        children_html = ""
        if include_children and self.children:
            # children_html = "\n\t"
            for child in self.children:
                children_html += child.html_string()

        return f"<{self.name}>{children_html}<{self.name}/>\n"
