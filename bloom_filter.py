from hashlib import sha1
from array import array
from math import *
from random import shuffle

class HashGenerator:

    def __init__(self):
        self.uniqueKey = 0

    def generateHash(self, m):
        unique = self.uniqueKey
        randSalt = list("this will be random")
        shuffle(randSalt)
        randSalt = ''.join(randSalt)
        def hashFunction(item):
            hashed = sha1(str(unique) + randSalt + str(item)).hexdigest()
            num = int(hashed[0:8], 16) % m
            return int(num)
        self.uniqueKey += 1
        return hashFunction

class BloomFilter:

    def __init__(self, c=0.01, n=1000, multiplier=1):
        self.amtOfItems = 0
        self.falsePosRate = c
        self.numOfKeys = n
        self.length, self.numOfHashes = self._calculateBloomFilterSettings()
        self.length = self.length * multiplier
        self.bFilter = self._createFreshFilter(int(self.length))
        self.hashes = self._generateHashes()

    def lookup(self, item):
        indexes = self._hashItem(item)
        found = True
        for i in indexes:
            if self.bFilter[i] == 0:
                found = False
                break
        return found

    def add(self, item):
        self.amtOfItems += 1
        bitsToFlip = self._hashItem(item)
        self.__flipBits(bitsToFlip)

    def addByList(self, listOfItems):
        [self.add(item) for item in listOfItems]

    def _hashItem(self, item):
        return [f(item) for f in self.hashes]

    def _generateHashes(self):
        generator = HashGenerator()
        hashes = []
        for i in xrange(int(self.numOfHashes)):
            hashes.append(generator.generateHash(self.length))
        return hashes

    def _createFreshFilter(self, m):
        freshFilter = array('b')
        for i in xrange(m):
            freshFilter.append(0)
        return freshFilter

    # def _getNumHashesWithFixedM(self, m, n):
    #     output = ceil(log(2) * m / n)
    #     return output

    def _calculateBloomFilterSettings(self):
        bestK = 1
        lowestM = None
        for num in xrange(1,101):
            m = (-1.0 * num * self.numOfKeys) / (log( 1 - (self.falsePosRate ** (1.0/num))))
            if m < lowestM or lowestM == None:
                lowestM = m
                bestK = num
        return (ceil(lowestM), bestK)

    def __flipBits(self, bitsToFlip):
        [self.__flipBit(int(i)) for i in bitsToFlip]

    def __flipBit(self, bitIndex):
        self.bFilter[bitIndex] = 1