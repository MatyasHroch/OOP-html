from abc import ABC, abstractmethod, abstractproperty


class Tag(ABC):
    """Abstract class, which defines html elements"""

    def __init__(self) -> None:
        self._classes: list[str] = []
        pass

    @abstractmethod
    def html_string(self, include_children=True) -> str:
        """Returns html string representation of the tag.
        Each tag should implement this method.
        It can also include all the children tags (acording to the include_children parameter)
        """
        pass

    @abstractproperty
    def name(self) -> str:
        pass

    @abstractproperty
    def attributes(self) -> dict:
        pass

    @abstractproperty
    def parent(self) -> "Tag":
        pass

    @parent.setter
    def parent(self, parent: "Tag"):
        pass

    @property
    def classes(self) -> list[str]:
        return self._classes

    @classes.setter
    def classes(self, classes: list[str]):
        classes_copy = classes.copy()
        self._classes = classes_copy
