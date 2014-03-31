from hashlib import sha1
from array import array
from math import *

class HashGenerator:

    def __init__(self):
        self.uniqueKey = 0
        self.salt = "salty"

    def generateHash(self, m):
        def hashFunction():
            hashed = sha1(str(self.uniqueKey) + self.salt).hexdigest()
            num = int(hashed[0:9], 16) % m
            return num
        self.uniqueKey += 1
        return hashFunction

class BloomFilter:

    def __init__(self, c=0.01, n=1000, m=None):
        self.falsePosRate = c
        self.numOfKeys = n
        if m == None:
            self.vectorLength, self.numOfHashes = self._calculateBloomFilterSettings()
        else:
            self.vectorLength = m
            self.numOfHashes = self._getNumHashesWithFixedM(m, n)
        bFilter = self._createFreshFilter(int(self.vectorLength))

    def _createFreshFilter(self, m):
        freshFilter = array('b')
        for i in xrange(m):
            freshFilter.append(0)
        return freshFilter

    def _getNumHashesWithFixedM(self, m, n):
        return ceil(log(2) * m / n)

    def _calculateBloomFilterSettings(self):
        bestK = 1
        lowestM = None
        for num in xrange(1,101):
            m = (-1.0 * num * self.numOfKeys) / (log( 1 - (.01 ** (1.0/num))))
            if m < lowestM or lowestM == None:
                lowestM = m
                bestK = num
        return (ceil(lowestM), bestK)

