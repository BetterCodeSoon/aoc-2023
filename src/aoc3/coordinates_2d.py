class Coordinates2d:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise Exception(f"Cannot compare other of type: {type(other)} to class type: {type(self)}")
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y))
