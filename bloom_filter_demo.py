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
        while len(mSet) <= maxLen:
            mSet.add(randint(m, n))
        return list(mSet)


def bloomFilterDemo():
    setGenerator = DemoSetGenerator()
    membershipSet = setGenerator.membershipSet
    testSet = setGenerator.testSet

    bloomFilter = BloomFilter(n=10000)
    bloomFilter.addByList(membershipSet)
    print "False Positive Rate at 0.01%:", testFalsePositiveRate(testSet, bloomFilter)

def testFalsePositiveRate(testSet, bloomFilter):
    length = len(testSet)
    amtTrue = 0.0
    for item in testSet:
        if bloomFilter.lookup(item):
            amtTrue += 1
    return round(amtTrue/length, 5)


bloomFilterDemo()