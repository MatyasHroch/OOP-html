from abc import ABC, abstractmethod, abstractproperty

from abstract_tags.tag import Tag


class PairTag(Tag):
    def __init__(self, children: list[Tag] = None) -> "PairTag":
        super().__init__()  # it will create __parent and __classes attributes
        if children is None:
            children = []
        self.__children = children or []

    def __add__(self, other: "Tag"):
        self.append_child(other)

    def append_child(self, other: "Tag"):
        if other is self or other in self.__children:
            raise ValueError(
                "Cannot add the tag to its own children or duplicate child."
            )

        self.__children.append(other)
        other.__parent = self

    @property
    def children(self) -> list["Tag"]:
        return self.__children.copy()

    @children.setter
    def children(self, children: list["Tag"]) -> "PairTag":
        children_copy = children.copy()
        self.__children = children_copy
        return self

    # TODO stringbuilder
    def html_string(self, include__children=True) -> str:
        children_html = ""
        if include__children and self.children:
            for child in self.children:
                children_html += f"\n{child.html_string()}"

        return f"<{self.name}>{children_html}\n<{self.name}/>"
