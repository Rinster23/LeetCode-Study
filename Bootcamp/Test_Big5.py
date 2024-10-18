import unittest
from collections import deque
from array import array
from sortedcontainers import SortedDict


class Test_Big5(unittest.TestCase):

    # Test a deque - Python's linked list
    def testDeque(self):

        # Testing append, appendleft, pop, popleft
        d = deque()
        for v in range(0, 10):
            d.append(v)

        # Random access using square brackets is supported
        # but NOT efficient. This is a linked list. We are 
        # using it for our tests: make sure the last 
        # element is 9.
        self.assertAlmostEqual(d[-1], 9)
        d.appendleft(20)
        self.assertAlmostEqual(d[0], 20)
        self.assertAlmostEqual(d.popleft(), 20)
        self.assertAlmostEqual(d.popleft(), 0)
        self.assertAlmostEqual(d[0], 1)
        self.assertAlmostEqual(d.pop(), 9)
        self.assertAlmostEqual(len(d), 8)

    # Test Python's equivalent of an array list,
    # something that looks like a list but is
    # actually backed by a contiguous array.
    # Note that this list allows mixed data
    # types.
    def testList(self):
        a = [None] * 20
        a[10] = "Hello"
        a[11] = 42
        self.assertAlmostEqual(len(a), 20)

    # Test Python's array. It's more efficient
    # than a list because it allows us to define
    # the data type up front.
    def testArray(self):

        # We declare an array of 20 integers:
        a = array("i", range(0, 20))
        self.assertAlmostEqual(len(a), 20)

        # Unlike the list, the array can take
        # only the data types we defined, in
        # this case, integers (as specified
        # by the "i" argument to the
        # constructor).
        a[5] = 200

        # We generate an exception if we try to
        # add a different data type.
        error = None
        try:
            a[5] = "hello"
        except Exception as e:
            error = e
        self.assertEqual(str(error), "'str' object cannot be interpreted as an integer")

    # Test dictionary, which is the equivalent of Java's
    # HashMap with the one exception that mixed data
    # types are allowed.
    def testDict(self):
        d = dict()
        d["lee"] = 55
        d[29] = 13
        # Overwrite previous value
        d[29] = 52
        self.assertAlmostEqual(d["lee"], 55)
        self.assertAlmostEqual(d[29], 52)
        self.assertAlmostEqual(len(d), 2)

    def testSet(self):
        s1 = set(range(0, 9))
        s2 = set(range(5, 15))

        # Differences
        self.assertTrue((s1 - s2) == set(range(0, 5)))
        self.assertTrue((s2 - s1) == set(range(9, 15)))
        # Union
        self.assertTrue((s1 | s2) == set(range(0, 15)))
        # Intersection
        self.assertTrue((s1 & s2) == set(range(5, 9)))
        # Symmetrical differences ^
        self.assertTrue((s1 ^ s2) == (set(range(0, 5)) | set(range(9, 15))))

    def testTree(self):
        s = SortedDict()
        s["a"] = "b"
        s["c"] = "d"
        s["b"] = "c"
        self.assertEqual(s.get("a"), "b")
        self.assertEqual(list(s.keys()), list(["a", "b", "c"]))
        s["e"] = "f"
        self.assertEqual(s.peekitem(-1), ("e", "f"))
        self.assertEqual(len(s), 4)


if __name__ == "__main__":
    unittest.main()
