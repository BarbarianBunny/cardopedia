try:
    # be ready for 3.11 when it drops
    from enum import StrEnum
except ImportError:
    from backports.strenum import StrEnum


class OrderedStrEnum(StrEnum):

    def __init__(self, *args):
        try:
            # attempt to init other parents in hierarchy
            super().__init__(*args)
        except TypeError:
            # ignore -- there are no other parents
            pass
        ordered = len(self.__class__.__members__) + 1
        self._order = ordered

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self._order < other._order
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self._order <= other._order
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self._order > other._order
        return NotImplemented

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self._order >= other._order
        return NotImplemented
