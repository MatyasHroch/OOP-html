from abc import ABC, abstractmethod

from abstract_tags.tag import Tag


class PairTag(Tag):
    """Represents a tag that can contain other tags inside.
    Each tag that can contain other tags should inherit from this class.
    """

    def __init__(self) -> "PairTag":
        """Constructor of the PairTag class, we set default values to the attributes all pair tags have in common."""
        super().__init__()
        self.__children = []

    def __add__(self, other: Tag):
        """Whenever we use the + operator on a PairTag, we add the other tag as a child of the PairTag."""
        self.append_child(other)

    @property
    def parent(self) -> "PairTag":
        """This class specifies the parent property as a PairTag"""
        return self.__parent

    @property
    def attributes(self) -> dict[str, str]:
        return super().attributes

    @property
    def children(self) -> list[Tag]:
        """Returns a copy of the children list."""
        return self.__children.copy()

    @children.setter
    def children(self, children: list[Tag]) -> "PairTag":
        """Sets the children list to the copy of the given list."""
        self.__children = children.copy()

    def append_child(self, other: Tag):
        """Adds the other tag as a child of the PairTag."""

        if other is self or other in self.__children:
            raise ValueError(
                "Cannot add the tag to its own children or duplicate child."
            )

        self.__children.append(other)
        other.__parent = self

    def append_children(self, others: list[Tag]):
        """Adds the others tags as children of the PairTag."""

        for other in others:
            self.append_child(other)

    def remove_child(self, other: Tag):
        """Removes the other tag from the children of the PairTag."""

        if other not in self.__children:
            raise ValueError("Cannot remove a child that is not in the children list.")

        self.__children.remove(other)
        other.__parent = None

    def html_string(self, include_children=True, depth=0) -> str:
        """Returns html string representation of all common pair tags.
        Because PairTag inherits from Tag, it has to implement the html_string method.
        """

        # we create a string of spaces for indentation
        indentation = "  " * depth
        attributes_str = ""

        # we create a string of all the attributes
        if self.attributes_str:
            attributes_str = f" {self.attributes_str}"

        # if there are children, we collect their html strings
        children_html = []
        if include_children and self.children:
            for child in self.children:
                children_html.append(child.html_string(depth=depth + 1))

        # instead of recreating the string every time we add a child, we can use a list and then join it
        children_html_str = "\n".join(children_html)

        # if there are children, we add a new line before and after the children html string
        if children_html_str:
            children_html_str = f"\n{children_html_str}\n{indentation}"

        name = self.name

        return f"{indentation}<{name}{attributes_str}>{children_html_str}<{name}/>"
