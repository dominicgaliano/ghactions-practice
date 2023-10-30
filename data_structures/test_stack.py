import unittest
from stack import Stack


class TestStackMethods(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(str(stack), "3 2 1")

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        lastElement = stack.pop()
        self.assertEqual(str(stack), "2 1")
        self.assertEqual(lastElement.value, 3)

    def test_push_head(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.head.value, 1)

    def test_pop_head(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        self.assertEqual(stack.head.value, 1)

    def test_pop_head_empty(self):
        stack = Stack()
        stack.push(1)
        stack.pop()
        self.assertEqual(stack.head, None)

    def test_pop_empty(self):
        stack = Stack()
        popped = stack.pop()
        self.assertEqual(popped, None)


if __name__ == "__main__":
    unittest.main()
