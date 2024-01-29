from abc import ABC, abstractmethod, abstractproperty

from abstract_tags.tag import Tag
from abstract_tags.pair_tag import PairTag


class LeafTag(Tag):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def html_string(self, include_children=True) -> str:
        return f"<{self.name}/>"
