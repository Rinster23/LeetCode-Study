from random import uniform
from Cluster import Cluster
from Point import Point


class PointSpace:
    def __init__(self):
        self._points = [
            Point([i, j])
            for i in range(100)
            for j in range(100)
        ]

    def sample(self, n):
        return [Cluster(sample[1]) for sample in sorted(
            (uniform(0, 1.0), point) for point in self._points)
                ][0:n]

    def pointsIterator(self):
        return iter(self._points)

    def get(self, index):
        return self._points[index]

    def getNPoints(self):
        return len(self._points)
