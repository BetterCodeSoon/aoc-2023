from dataclasses import dataclass

R = "red"
G = "green"
B = "blue"


@dataclass
class CubeContainer:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue
