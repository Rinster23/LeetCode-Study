import math
import unittest
import random
import Shuffler

random.seed(137452)


def ShufflingSimulation(shuffleFunc, listOfValues, nRuns):
    # Compute expectation of nRuns
    expectedSum = nRuns * sum(listOfValues) / len(listOfValues)
    # Initialize array of sums to zero
    observedSums = [0] * len(listOfValues)
    # Perform n runs
    for iRun in range(nRuns):
        # Make a copy of the list of values
        aList = list(listOfValues)
        # Call shuffling function that was passed in
        aList = shuffleFunc(aList)
        # Update sum of each position in the list using
        # value placed there by the shuffle
        for iPlace in range(len(aList)):
            observedSums[iPlace] += aList[iPlace]
    # Return both the expected sum -- one value -- and the
    # actual sums obtained for each position by the
    # simulation
    return [expectedSum, observedSums]


class Test_Shuffler(unittest.TestCase):
    def testNN(self):
        nBins = 10
        nRuns = 10000
        expectedSum, observedSums = ShufflingSimulation(
            shuffleFunc=Shuffler.shuffleN,
            listOfValues=range(nBins),
            nRuns=nRuns
        )
        self.assertEqual(
            "[44815, 45067, 45046, 44698, 45053, 45290, 45079, 44883, 44987, 45082]",
            str(observedSums)
        )

    def testNLogN(self):
        nBins = 10
        nRuns = 10000
        expectedSum, observedSums = ShufflingSimulation(
            shuffleFunc=Shuffler.shuffleNLogN,
            listOfValues=range(nBins),
            nRuns=nRuns
        )
        self.assertEqual(
            '[44883, 45624, 44700, 45268, 45055, 44780, 44498, 44800, 45336, 45056]',
            str(observedSums)
        )

    def testN(self):
        nBins = 10
        nRuns = 10000
        expectedSum, observedSums = ShufflingSimulation(
            shuffleFunc=Shuffler.shuffleN,
            listOfValues=range(nBins),
            nRuns=nRuns
        )
        self.assertEqual(
            '[44845, 44755, 44777, 45471, 45317, 44716, 44975, 44706, 44991, 45447]',
            str(observedSums)
        )

    def testStatistics(self):
        # Set parameters of our binomial distribution
        nBins = 2
        nRuns = 10000
        # Compute standard deviation
        sd = math.sqrt(nRuns * 0.5 * 0.5)
        # Enumerate the functions we're testing
        testFuncs = [
            Shuffler.shuffleNN,
            Shuffler.shuffleNLogN,
            Shuffler.shuffleN
        ]
        # Iterate through functions we're testing and
        # call shuffle for each
        for testFunc in testFuncs:
            # Shuffle
            expectedSum, observedSums = ShufflingSimulation(
                shuffleFunc=testFunc,
                listOfValues=range(nBins),
                nRuns=nRuns
            )
            # Did any of the sums violate 2 sigma expectations?
            for observedSum in observedSums:
                if math.fabs(observedSum - expectedSum) > (2 * sd):
                    # This one did, so raise an exception
                    raise Exception("Failed two sigma test")


if __name__ == '__main__':
    unittest.main()
