import unittest
import datetime
from collections import deque


class ListVSDeque(unittest.TestCase):
    @classmethod
    def f1(cls):
        aList = list()
        for i in range(1000000):
            aList.append(i)
            if i > 3600:
                aList.pop(0)
        return [len(aList), aList[0], aList[-1]]

    @classmethod
    def f2(cls):
        aDeck = deque()
        for i in range(1000000):
            aDeck.append(i)
            if i > 3600:
                aDeck.popleft()
        return [len(aDeck), aDeck[0], aDeck[-1]]

    def testTiming(self):
        # List timing
        start = datetime.datetime.now()
        result = ListVSDeque.f1()
        end = datetime.datetime.now()
        listResults = (end - start, result)
        # Deque timing
        start = datetime.datetime.now()
        result = ListVSDeque.f2()
        end = datetime.datetime.now()
        dequeResults = (end - start, result)
        # Display difference
        print("List: " + str(listResults))
        print("Deque: " + str(dequeResults))


if __name__ == '__main__':
    unittest.main()
