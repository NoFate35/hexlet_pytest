import operator


class Node:
    def __init__(self, key, left=None, right=None):
        """Create a new tree node."""
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        if self is None:
            return None
        rd = ""
        rd += str(self.__class__.__name__)
        rd += f"({self.key}, {self.__repr__(self.left)}, {self.__repr__(self.right)})"
        print("rd", rd)
        return rd