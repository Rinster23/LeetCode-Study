class KMeans:
    def __init__(self, pointSpace, initialClusters):
        self._clusters = initialClusters
        self._pointSpace = pointSpace
        self._generation = 0

    def meanSqDistance(self):
        sumDist = 0.0
        for cluster in self._clusters:
            for point in cluster.points():
                sumDist += cluster.getDistance(point)
        return sumDist / self._pointSpace.getNPoints()

    def run(self):
        while True:
            self.recalc()
            self.report()
            if self.hasConverged():
                break
        self.finalReport()

    def report(self):
        print(
            "Generation %d: mean sq distance = %.3f" % (
                self._generation,
                self.meanSqDistance()
            )
        )

    def recalc(self):
        for point in self._pointSpace.pointsIterator():
            point.addSelfToNearest(iter(self._clusters))
        for cluster in self._clusters:
            cluster.scale()
        self._generation += 1

    def hasConverged(self):
        return all(not cluster.hasMoved(0.001) for cluster in self._clusters)

    def getCluster(self, index):
        return self._clusters[index]

    def finalReport(self):
        for cluster in self._clusters:
            print(str(cluster))
