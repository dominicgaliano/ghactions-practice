from nodes import BinaryTreeNode
from queue import Queue


class BST:
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def isEmpty(self):
        return self.root is None

    def size(self):
        return self.nodeCount

    def add(self, elem):
        # if contains already, do not add
        if self.contains(elem):
            return False

        # recurse
        self.root = self.addRecursively(self.root, elem)
        self.nodeCount += 1

    # private function to recursively add element
    def addRecursively(self, node, elem):
        # Null node found, place child
        if node is None:
            return BinaryTreeNode(elem)

        if elem < node.value:
            node.left = self.addRecursively(node.left, elem)
            return node

        node.right = self.addRecursively(node.right, elem)
        return node

    def remove(self, elem):
        if self.contains(elem):
            self.root = self.removeRecursively(self.root, elem)
            self.nodeCount -= 1
            return True
        return False

    # private function to recursively remove element
    def removeRecursively(self, node, elem):
        if node is None:
            return None

        # search tree for node:
        # element expected down left branch
        if elem < node.value:
            node.left = self.removeRecursively(node.left, elem)

        # element expected down right branch
        elif elem > node.value:
            node.right = self.removeRecursively(node.right, elem)

        else:
            # node for removal found
            # determine case
            left = node.left
            right = node.right
            # no subtrees or only right subtree (case 1 and 3)
            if not left:
                return right
            # left subtree exists (case 2)
            if not right:
                return left

            # case 4 (has left and right subtrees)
            # find largest value in left subtree
            largestLeft = self.findMax(left)

            # swap data
            node.value = largestLeft.value

            node.left = self.removeRecursively(node.left, largestLeft.value)

        return node

    def findMin(self, node):
        # keep going left
        while node.left:
            node = node.left

        return node

    def findMax(self, node):
        # keep going right
        while node.right:
            node = node.right

        return node

    def contains(self, elem):
        return self.containsRecursively(self.root, elem)

    # private function to recursively search for element
    def containsRecursively(self, node, elem):
        # null node reached
        if node is None:
            return False

        # comparisons
        # equal
        if node.value == elem:
            return True
        # node less than elem, recurse right
        elif node.value < elem:
            return self.containsRecursively(node.right, elem)
        # node greater than elem, recurse left
        return self.containsRecursively(node.left, elem)

    def height(self):
        return self.heightRecursively(self.root)

    def heightRecursively(self, node):
        if node is None:
            return 0
        return (
            max(
                self.heightRecursively(node.left),
                self.heightRecursively(node.right),
            )
            + 1
        )

    def traverse(self, order):
        if order == "preorder":
            self.preorder(self.root)
        elif order == "inorder":
            self.inorder(self.root)
        elif order == "postorder":
            self.postorder(self.root)
        elif order == "levelorder":
            self.levelorder(self.root)
        else:
            raise ValueError

    def preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)

    def levelorder(self, node):
        # Let Q by a Queue
        # Q.enqueue(starting_node)
        # starting_node.visited = true

        # While Q in not empty Do

        # node = Q.dequeue()

        # For neighbor in neighbors(node):
        #     If neighbor has not been visited:
        #     neighbor.visited = true
        #     Q.enqueue(neighbor)
        q = Queue()
        q.enqueue(node)
        visited = set()
        visited.add(node)

        while not q.isEmpty():
            node = q.dequeue()
            print(node.value)

            children = [node.left, node.right]
            for child in children:
                if child and child not in visited:
                    visited.add(child)
                    q.enqueue(child)


def main():
    bst = BST()
    bst.add(11)
    bst.add(10)
    bst.add(2)
    bst.add(1)
    bst.add(13)
    bst.add(8)
    bst.add(13)
    bst.add(12)
    bst.add(15)
    bst.add(12)
    bst.add(9)
    bst.add(3)
    bst.traverse("preorder")
    print("------")
    bst.traverse("inorder")
    print("------")
    bst.traverse("postorder")
    print("------")
    bst.traverse("levelorder")
    print("------")


if __name__ == "__main__":
    main()
