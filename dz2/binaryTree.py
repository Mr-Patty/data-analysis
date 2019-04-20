from collections import deque

class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.value = x

    def getValue(self):
        return self.value

    def __iter__(self):
        yield self

    def __contains__(self, item):
        if self.value == item:
            return True
        elif self.left and item < self.value:
            return item in self.left
        elif self.right and item >= self.value:
            return item in self.right
        else:
            return False


class BinarySearchTree:
    def __init__(self, value = None):
        if value is None:
            self.root = None
        else:
            self.root = Node(value)

    def put(self, val, currRoot):
        if val == currRoot.getValue():
            return self
        elif val < currRoot.getValue():
            if currRoot.left is None:
                currRoot.left = Node(val)
            else:
                self.put(val, currRoot.left)
        else:
            if currRoot.right is None:
                currRoot.right = Node(val)
            else:
                self.put(val, currRoot.right)

    def append(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self.put(x, self.root)

    def __iter__(self):
        if self.root is None:
            return
        dq = deque(self.root)
        while dq:
            a = dq.popleft()
            yield a.getValue()
            if a.left:
                dq.append(a.left)
            if a.right:
                dq.append(a.right)

    def __contains__(self, item):
        if self.root is None:
            return False
        else:
            return item in self.root



if __name__ == '__main__':
    tree = BinarySearchTree(8)
    for v in [8, 3, 10, 1, 6, 4, 14, 13, 7]:
        tree.append(v)

    for v in [8, 12, 13, 15]:
        print(v in tree)

    print(*tree)

    tree = BinarySearchTree()
    for v in [5, 0, 6, 2, 1, 3]:
        tree.append(v)

    for v in [6, 12]:
        print(v in tree)

    print(*tree)
