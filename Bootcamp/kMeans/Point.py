import math


class Point:
    def __init__(self, coords):
        # Skip validation for now
        self._coords = coords

    def getCoord(self, index):
        # Skip validation for now
        return self._coords[index]

    def getNDims(self):
        return len(self._coords)

    def getDistance(self, otherPoint):
        # Skip validation that otherPoint is a Point
        if self.getNDims() != otherPoint.getNDims():
            raise Exception("Other point has different number of dimensions")
        return sum(
            math.pow(self.getCoord(i) - otherPoint.getCoord(i), 2.0) for i in range(self.getNDims()))

    def plus(self, otherPoint):
        # Skip validation that other point is a Point
        # and has the same number of dimensions
        newCoords = list([0] * self.getNDims())
        for i in range(self.getNDims()):
            newCoords[i] = self.getCoord(i) + otherPoint.getCoord(i)
        return Point(newCoords)

    def scale(self, scalingFactor):
        newCoords = [c * scalingFactor for c in self._coords]
        return Point(newCoords)

    def addSelfToNearest(self, clusters):
        nearestCluster = next(clusters)
        for cluster in clusters:
            if cluster.getDistance(self) < nearestCluster.getDistance(self):
                nearestCluster = cluster
        nearestCluster.addPoint(self)
        return nearestCluster

    def __str__(self):
        return "Point(%s)" % str(self._coords)
