import unittest
from KMeans import KMeans
from PointSpace import PointSpace


class Test_KMeans(unittest.TestCase):
    def test1Cluster(self):
        pointspace = PointSpace()
        nClusters = 1
        initialClusters = pointspace.sample(nClusters)
        kmeans = KMeans(pointspace, initialClusters)
        kmeans.run()
        cluster = kmeans.getCluster(0)
        self.assertEqual('Cluster(centroid=Point([49.5, 49.5]))', str(cluster))

    def test4Cluster(self):
        pointspace = PointSpace()
        nClusters = 4
        initialClusters = pointspace.sample(nClusters)
        kmeans = KMeans(pointspace, initialClusters)
        kmeans.run()
        results = str(list(sorted(str(kmeans.getCluster(i)) for i in range(4))))
        cluster = kmeans.getCluster(0)
        self.assertEqual(
            "['Cluster(centroid=Point([24.5, 24.5]))', 'Cluster(centroid=Point([24.5, 74.5]))', 'Cluster(centroid=Point([74.5, 24.5]))', 'Cluster(centroid=Point([74.5, 74.5]))']",
            results
        )


if __name__ == '__main__':
    unittest.main()
