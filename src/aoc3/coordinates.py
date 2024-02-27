from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)
