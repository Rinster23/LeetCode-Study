import math
from collections import deque
from Point import Point


class Cluster:
    def __init__(self, centroid):
        self._prevPoints = None
        self._prevCentroid = None
        self._centroid = centroid
        self._points = deque()
        self._pointsAccumulator = Point([0] * centroid.getNDims())

    def getCentroid(self):
        return self._centroid

    def getDistance(self, point):
        return point.getDistance(self.getCentroid())

    def addPoint(self, point):
        self._points.append(point)
        self._pointsAccumulator = self._pointsAccumulator.plus(point)

    def scale(self):
        self._prevCentroid = self._centroid
        self._centroid = self._pointsAccumulator.scale(1.0 / len(self._points))
        self._pointsAccumulator = Point([0] * self._centroid.getNDims())
        self._prevPoints = self._points
        self._points = deque()

    def hasMoved(self, tolerance):
        return math.fabs(self._centroid.getDistance(self._prevCentroid)) > tolerance

    def points(self):
        return iter(self._prevPoints)

    def __str__(self):
        return "Cluster(centroid=%s)" % str(self._centroid)
