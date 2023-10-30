import unittest
from priorityQueue import PQueue


class TestPriorityQueueMethods(unittest.TestCase):
    def test_add_sequential(self):
        pq = PQueue()
        pq.add(1)
        pq.add(2)
        pq.add(3)
        self.assertEqual(pq.heap, [1, 2, 3])

    def test_add_nonsequential(self):
        pq = PQueue()
        pq.add(10)
        pq.add(9)
        pq.add(8)
        pq.add(7)
        self.assertEqual(pq.heap, [7, 8, 9, 10])

    def test_peek(self):
        pq = PQueue()
        pq.add(10)
        pq.add(9)
        pq.add(8)
        pq.add(7)
        self.assertEqual(pq.peek(), 7)

    def test_poll(self):
        pq = PQueue()
        pq.add(10)
        pq.add(9)
        pq.add(8)
        pq.add(7)
        element = pq.poll()
        self.assertEqual(element, 7)
        self.assertEqual(pq.heap, [8, 10, 9])

    def test_removeAt_internal(self):
        pq = PQueue()
        pq.add(1)
        pq.add(2)
        pq.add(3)
        pq.add(4)
        pq.add(5)
        pq.add(6)
        pq.add(7)
        pq.add(8)
        pq.add(9)
        # [1,2,3,4,5,6,7,8,9]
        removed = pq.removeAt(3)
        # [1,2,3,none,5,6,7,8,9]
        # [1,2,3,9,5,6,7,8]
        # [1,2,3,8,5,6,7,9]
        self.assertEqual(pq.heap, [1, 2, 3, 8, 5, 6, 7, 9])
        self.assertEqual(removed, 4)

    def test_removeAt_leaf(self):
        pq = PQueue()
        pq.add(3)
        pq.add(5)
        pq.add(7)
        pq.add(9)
        pq.add(11)
        pq.add(13)
        removed = pq.removeAt(4)
        self.assertEqual(pq.heap, [3, 5, 7, 9, 13])
        self.assertEqual(removed, 11)

    def test_remove_internal(self):
        pq = PQueue()
        pq.add(1)
        pq.add(2)
        pq.add(3)
        pq.add(4)
        pq.add(5)
        pq.add(6)
        pq.add(7)
        pq.add(8)
        pq.add(9)
        # [1,2,3,4,5,6,7,8,9]
        removed = pq.remove(4)
        # [1,2,3,none,5,6,7,8,9]
        # [1,2,3,9,5,6,7,8]
        # [1,2,3,8,5,6,7,9]
        self.assertEqual(pq.heap, [1, 2, 3, 8, 5, 6, 7, 9])
        self.assertEqual(removed, 4)

    def test_remove_leaf(self):
        pq = PQueue()
        pq.add(3)
        pq.add(5)
        pq.add(7)
        pq.add(9)
        pq.add(11)
        pq.add(13)
        removed = pq.remove(11)
        self.assertEqual(pq.heap, [3, 5, 7, 9, 13])
        self.assertEqual(removed, 11)


if __name__ == "__main__":
    unittest.main()
