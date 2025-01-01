class Counter:

    def __init__(self, count: int = 0):
        if count < 0:
            raise ValueError(f"The count: {count} is < 0. Count can only be 0 or bigger.")
        self.count = count

    def count_up(self):
        self.count += 1

    def count_down(self):
        if self.count > 0:
            self.count -= 1

    def __eq__(self, other):
        if isinstance(other, Counter):
            return self.count == other.count
        return False
