from abc import ABC, abstractmethod


class Tag:
    """Abstract class, which defines html tags"""

    def __init__(self) -> None:
        self.__parent = None
        self.__classes = []

    @abstractmethod
    def html_string(self, include_children=True) -> str:
        """Returns html string representation of the tag.
        Each tag should implement this method.
        It can also include all the children tags (acording to the include_children parameter)
        """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def attributes(self) -> dict:
        pass

    @attributes.setter
    def attributes(self, attributes: dict):
        pass

    @property
    def classes(self) -> list[str]:
        return self._classes

    @classes.setter
    def classes(self, classes: list[str]):
        classes_copy = classes.copy()
        self._classes = classes_copy

    @abstractmethod
    @property
    def parent(self) -> "Tag":
        pass
