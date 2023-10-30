import unittest
from binarySearchTree import BST


class TestBSTMethods(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.bst.add(11)
        self.bst.add(10)
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(13)
        self.bst.add(8)
        self.bst.add(13)
        self.bst.add(12)
        self.bst.add(15)
        self.bst.add(12)
        self.bst.add(9)
        self.bst.add(3)

    def test_isempty(self):
        emptyBst = BST()
        self.assertTrue(emptyBst.isEmpty())
        self.assertFalse(self.bst.isEmpty())

    def test_size(self):
        self.assertEqual(self.bst.size(), 10)

    def test_add(self):
        self.bst.add(7)
        self.assertEqual(self.bst.size(), 11)
        self.assertTrue(self.bst.contains(7))
        self.assertEqual(self.bst.height(), 6)

    def test_remove(self):
        self.bst.remove(8)
        self.assertEqual(self.bst.size(), 9)
        self.assertFalse(self.bst.contains(8))
        self.assertEqual(self.bst.height(), 5)

    def test_contains(self):
        self.assertFalse(self.bst.contains(0))
        self.assertTrue(self.bst.contains(15))

    def test_height(self):
        self.assertEqual(self.bst.height(), 5)

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
