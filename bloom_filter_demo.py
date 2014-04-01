from sets import Set 
from random import randint
from bloom_filter import *

class DemoSetGenerator:

    def __init__(self):
        lgSet = self.generateUniqueList(20000, 10000, 99999)
        self.membershipSet = lgSet[0:10000]
        self.testSet = lgSet[10000:]


    def generateUniqueList(self, maxLen, m, n):
        mSet = Set([])
        while len(mSet) < maxLen:
            mSet.add(randint(m, n))
        return list(mSet)


def bloomFilterDemo():
    setGenerator = DemoSetGenerator()
    membershipSet = setGenerator.membershipSet
    testSet = setGenerator.testSet

    bloomFilter = BloomFilter(n=10000)
    bloomFilter.addByList(membershipSet)
    test = testFalsePositiveRate(testSet, bloomFilter)
    print "False Positive Rate at 1% resulted in:", str(test[0]) + "%"
    print "Collisions at 1%:", test[1]
    print

    bloomFilter = BloomFilter(c=.001, n=10000)
    bloomFilter.addByList(membershipSet)
    test = testFalsePositiveRate(testSet, bloomFilter)
    print "False Positive Rate at .1% resulted in:", str(test[0]) + "%"
    print "Collisions at .1%:", test[1]
    print

    bloomFilter = BloomFilter(c=.0001, n=10000)
    bloomFilter.addByList(membershipSet)
    test = testFalsePositiveRate(testSet, bloomFilter)
    print "False Positive Rate at .01% resulted in:", str(test[0]) + "%"
    print "Collisions at .01%:", test[1]

def testFalsePositiveRate(testSet, bloomFilter):
    length = len(testSet)
    amtTrue = 0.0
    for item in testSet:
        if bloomFilter.lookup(item):
            amtTrue += 1
    print length
    return (round(amtTrue/length, 10) * 100, amtTrue)


bloomFilterDemo()