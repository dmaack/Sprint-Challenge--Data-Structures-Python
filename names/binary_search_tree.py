# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        root = self
        new_node = BinarySearchTree(value)

        if value < root.value:
            if root.left is None:
                root.left = new_node
            else:
                root.left.insert(value)
        elif value >= root.value:
            if root.right is None:
                root.right = new_node
            else: 
                root.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value < target:
            if self.right is None:
                return None
            else:
                return self.right.contains(target)
        elif self.value >= target:
            if self.left is None:
                return None
            else:
                self.left.contains(target)
        else:
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        root = self

        if root.right is None:
            return root.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


