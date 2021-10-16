class BinaryTree:
    """Binary tree structure for storing item codes and their prices"""
    def __init__(self, code, price):
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
        """Method that creates a new node in the tree"""
        if not isinstance(code, int):
            raise TypeError("Item code should be an integer type value!")
        if not isinstance(price, (int, float)):
            raise TypeError("Items price should be an integer or float value!")
        if not self.code:
            self.code = code
            self.price = price
            return
        if code < self.code:
            if self.left:
                self.left.insert(code, price)
                return
            self.left = BinaryTree(code, price)
            return
        if self.right:
            self.right.insert(code, price)
            return
        self.right = BinaryTree(code, price)

    def find(self, code, volume):
        """Method for finding an item by its code returns its price multiplied by volume provided in input"""
        if not isinstance(volume, int):
            raise TypeError("Volume of items should be integer type value!")
        if code == self.code:
            return self.price * volume
        if code < self.code:
            if self.left:
                return self.left.find(code, volume)
        else:
            if self.right:
                return self.right.find(code, volume)
        raise ValueError("Searched code doesnt exist in this tree")


def main():
    root = BinaryTree(13, 16.5)
    root.insert(15, 20)
    root.insert(10, 12)
    root.insert(11, 14.2)
    root.insert(1, 34)
    print(root.find(1, 10))
    print(root.find(15, 2))


if __name__ == '__main__':
    main()

