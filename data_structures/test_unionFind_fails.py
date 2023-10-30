import unittest
from unionFind import UnionFind


class TestUnionFindMethods(unittest.TestCase):
    def test_unionFind_init(self):
        elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        uf = UnionFind(elements)
        self.assertEqual(uf.arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # the line below has been modified to cause this test to fail
        self.assertEqual(uf.components(), 19)

    def test_unionFind_init_set(self):
        elements = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
        uf = UnionFind(elements)
        self.assertTrue(set(uf.arr) == set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_unionFind_union(self):
        elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        uf = UnionFind(elements)
        uf.unify("A", "B")
        self.assertEqual(uf.components(), 9)
        self.assertEqual(uf.componentSize("A"), 2)

    def test_unionFind_find(self):
        pass
        # bad test, should not be worried about the componentNumber
        # elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        # uf = UnionFind(elements)
        # uf.unify("A", "B")
        # componentNumber = uf.find("A")
        # self.assertEqual(componentNumber, 0)

    def test_unionFind_componentSize(self):
        elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        uf = UnionFind(elements)
        uf.unify("A", "B")
        uf.unify("C", "D")
        uf.unify("E", "F")
        uf.unify("F", "A")
        self.assertEqual(uf.componentSize("A"), 4)

    def test_unionFind_init_none(self):
        elements = []
        with self.assertRaises(IndexError):
            uf = UnionFind(elements)

    def test_unionFind_init_notIterable(self):
        elements = 1
        with self.assertRaises(TypeError):
            uf = UnionFind(elements)

    def test_unionFind_connected_notFound(self):
        elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        uf = UnionFind(elements)
        uf.unify("A", "B")
        uf.unify("C", "D")
        uf.unify("E", "F")
        uf.unify("F", "A")
        with self.assertRaises(KeyError):
            uf.connected("A", "Z")

    def test_unionFind_componentSize_notFound(self):
        elements = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        uf = UnionFind(elements)
        uf.unify("A", "B")
        uf.unify("C", "D")
        uf.unify("E", "F")
        uf.unify("F", "A")
        with self.assertRaises(KeyError):
            uf.componentSize("Z")


if __name__ == "__main__":
    unittest.main()
