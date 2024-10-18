import math
import unittest


class BasicBasics(unittest.TestCase):

    # Integers
    def test_int(self):
        i = 52
        j = 49
        self.assertEqual(101, i + j)
        self.assertEqual(300, int(300.7))
        self.assertEqual(300, int("300"))
        error = None
        try:
            int("300.7")
        except Exception as err:
            error = err
        self.assertFalse(error is None)
        self.assertEqual(300, int(float("300.7")))

    # Floats
    def testFloats(self):
        e = 4.00001
        f = 4.00000

        # Integer division with floats
        i = e // f
        self.assertEqual(1, i)
        j = f // e
        self.assertEqual(0, j)

        # Floating point division
        g = e / f

        # Float comparisons with tolerance
        # Never compare without tolerance!
        # The following are equivalent.
        numSignificantPlaces = 5
        self.assertAlmostEqual(1.0, g, numSignificantPlaces)
        self.assertTrue(math.fabs(g - 1.0) <= math.pow(10.0, -numSignificantPlaces))
        # The following are equivalent.
        numSignificantPlaces = 6
        self.assertNotAlmostEqual(1.0, g, numSignificantPlaces)
        self.assertFalse(math.fabs(g - 1.0) <= math.pow(10.0, -numSignificantPlaces))

        # Rounding, floor and ceiling
        self.assertEqual(1, round(g))
        self.assertEqual(2, round(g + 0.5))
        self.assertEqual(1, math.floor(g + 0.5))
        self.assertEqual(2, math.ceil(g))

    def testBool(self):
        b = 5 > 3
        self.assertTrue(b)
        b = 3.17
        self.assertTrue(b)
        self.assertFalse(b is True)
        b = 0.0
        self.assertFalse(b)
        self.assertEqual(False, b)
        self.assertFalse(b is False)

    # Strings
    def testStrings(self):
        string1 = "Lee Maclin"
        self.assertEqual(10, len(string1))
        string2 = "The professor's name is %s." % string1
        self.assertEqual("The professor's name is Lee Maclin.", string2)
        self.assertEqual("Lee", string1[0:3])
        self.assertEqual("Maclin", string1[-6:])
        self.assertEqual("i", string1[-2])
        self.assertEqual("Lee Macattack", string1.replace("lin", "attack"))

    # For loops
    def testForLoops(self):
        sum = 0
        for i in range(0, 7):
            if i == 3:
                continue
            if i == 5:
                break
            sum += i
        self.assertEqual(sum, 7)

    # While loops
    def testWhileLoops(self):
        q = list([1, 3, 13, 22])
        s = 0
        while len(q) > 0:
            s += q.pop(0)
            if (s + 5) % 7 == 0:
                break
            s += 5
        self.assertEqual(9, s)

    # If-then-else
    def testIfThenElse(self):
        if 5 > 6:
            raise Exception("What!?")
        else:
            if 6 == 5:
                raise Exception("Say what!?")
            elif 6 > 5:
                self.assertTrue(True)
            else:
                raise Exception("No way!")
        title = "professor"
        name = "Lee Maclin" if title == "professor" else "Bob Smith"
        self.assertEqual("Lee Maclin", name)

    def testChar(self):
        o = ord("A")
        # 'o' now contains the integer encoding of the
        # character "A", which is 65.
        self.assertEqual(65, o)
        # And this is how we convert it back to a character.
        c = chr(o)
        self.assertEqual("A", c)
        # A string is just a collection of characters.
        self.assertEqual("Ah!", c + "h!")

    # If we want to work with a mutable structure of raw
    # bytes instead of characters, we can use bytearray.
    def test_bytearray(self):
        b = bytearray("Hello", encoding="utf-8")
        self.assertEqual("Hello", b.decode("utf-8"))
        for c in ", there!":
            b.append(ord(c))
        self.assertEqual("Hello, there!", b.decode("utf-8"))
        exc = ord("!")
        self.assertEqual(33, exc)
        self.assertEqual(33, b[-1])
        # Note that the main difference between 'bytes'
        # and 'bytearray' is that the former is immutable.

    # If we need type enforcement, we can use 'array'
    # instead of 'list'. With 'array', we can specify
    # a type.
    def test_array(self):
        from array import array
        a = array('f')
        a.append(29)
        a.append(30.2)
        error = None
        try:
            a.append("H")
        except Exception as err:
            error = err
        self.assertEqual("must be real number, not str", str(error))

    def test_set(self):
        s = set()
        s.add('a')
        s.add('b')
        s.add('d')
        s1 = set()
        s1.add('b')
        s1.add('c')
        # union
        self.assertEqual(s | s1, set(['a', 'b', 'c', 'd']))
        # intersection
        self.assertEqual(s & s1, set(['b']))
        # difference
        self.assertEqual(s - s1, set(['a', 'd']))
        self.assertEqual(s1 - s, set(['c']))
        # symmetric difference
        d = s ^ s1
        self.assertEqual(d, set(['c', 'd', 'a']))

    def test_dict(self):
        d = dict()
        d["2319837"] = {"name": "Lee Maclin", "count": 0}
        d["8933018"] = {"name": "Bob Johnson", "count": 0}
        d["2319837"]["count"] += 1
        self.assertGreater(d["2319837"]["count"], d["8933018"]["count"])
        # Getting a list of keys
        keys = d.keys()
        self.assertEqual(['2319837', '8933018'], [key for key in keys])
        # Getting a list of values
        values = d.values()
        # Keys are unique so storing a value at an existing key
        # overwrites the original value
        d["8933018"] = {"name": "Eric Monse", "count": 20}
        s = str(d["8933018"])
        self.assertEqual("{'name': 'Eric Monse', 'count': 20}", s)
        # Getting a full string representation of a dictionary
        srep = str(d)
        self.assertEqual(
            "{'2319837': {'name': 'Lee Maclin', 'count': 1}, '8933018': {'name': 'Eric Monse', 'count': 20}}",
            srep
        )

    def test_list(self):
        l = list()
        for i in range(20):
            l.append(i)
        # Allows indexing from the end
        self.assertEqual(
            "[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]",
            str(l[-10:])
        )
        # Allows mixed data types
        l.append("Hello")
        # Remove data anywhere in the list
        self.assertEqual(2, l.pop(2))
