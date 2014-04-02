from hashlib import sha1
from array import array
from math import *
from random import shuffle

class HashGenerator:

    def generateHash(self, m):
        randSalt = list("this will be random")
        shuffle(randSalt)
        randSalt = ''.join(randSalt)
        def hashFunction(item):
            hashed = sha1(randSalt + str(item)).hexdigest()
            num = int(hashed[0:8], 16) % m
            return int(num)
        return hashFunction

class BloomFilter:

    def __init__(self, c=0.01, n=1000, multiplier=1, m=None):
        self.amtOfItems   = 0
        self.falsePosRate = c
        self.numOfKeys    = n        
        if m == None:
            self.length = self._calculateLength(self.falsePosRate, self.numOfKeys)
        else:
            self.length = m
        self.numOfHashes  = self._calculateNumOfHashes(self.length, self.numOfKeys)
        self.length       = ceil(self.length * multiplier)
        self.vector       = self._createFreshFilter(int(self.length))
        self.hashes       = self._generateHashes()

    def lookup(self, item):
        indexes = self._hashItem(item)
        found = True
        for i in indexes:
            if self.vector[i] == 0:
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
        return array('b', [0] * m)

    def _calculateNumOfHashes(self, m, n):
        return int(ceil((m / n) * .7))

    def _calculateLength(self, c, n):
        return abs(int(ceil((n * log(c)) / log(2) ** 2)))

    def __flipBits(self, bitsToFlip):
        [self.__flipBit(int(i)) for i in bitsToFlip]

    def __flipBit(self, bitIndex):
        self.vector[bitIndex] = 1