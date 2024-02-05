class Tag:
    """Abstract class, which defines html tags"""

    def __init__(self) -> None:
        """Constructor of the Tag class, we set default values to the attributes."""

        # We can add attributes, where we need some checks or additional logic
        self._parent: "Tag" = None
        self.__classes: list[str] = []

        # We can add attributes, where we don't need any checks or additional logic
        self.title: str = None
        self.id: str = None
        self.lang: str = None

    def __str__(self):
        """Returns html string representation of the tag anytime it is casted to string"""
        return self.html_string()

    @property
    def name(self) -> str:
        """Returns the name of the tag.
        By default it returns the lower case name of the class.
        If we want to print other name for the tag than the class name,
        we can just override this name property in the child class.
        """
        return self.__class__.__name__.lower()

    @property
    def classes(self) -> list[str]:
        """Returns a copy of the classes list."""
        return self.__classes.copy()

    @classes.setter
    def classes(self, classes: list[str]):
        """Sets the classes list to the copy of the given list."""
        self.__classes = classes.copy()

    @property
    # @abstractmethod
    def parent(self) -> "Tag":
        """Returns the parent of the tag.
        At this level we use the Tag class as the type of the parent.
        Later we can specify the type of the parent in the child classes.
        """
        return self._parent

    @property
    def attributes(self) -> dict[str, str]:
        """Returns a dictionary of all the attributes of the tag.
        Each tag should implement this property and call the parent's attributes property.
        So we can collect all the attributes of the tag in one place using an inheritance.
        """
        return {
            "title": self.title,
            "id": self.id,
            "lang": self.lang,
            "class": " ".join(self.classes),
        }

    @property
    def attributes_str(self) -> str:
        """Returns a string representation of all the attributes of the tag."""

        attributes = self.attributes

        # we get rid of the class attribute if it is empty
        if not attributes["class"]:
            del attributes["class"]

        return " ".join(
            [
                f'{key}="{value}"'
                for key, value in attributes.items()
                if value is not None
            ]
        )

    def append_class(self, class_name: str):
        """Adds the given class to the list of classes.
        We can add the same class multiple times, because it is possible in html.
        """
        self.__classes.append(class_name)

    def html_string(self, include_children=True, depth=0) -> str:
        """Each tag that inherits from the Tag class should implement this method.
        It should return the html string representation of the tag.
        It can also include all the children tags (acording to the include_children parameter).
        The depth parameter should be used for indentation.
        """
        return NotImplemented
