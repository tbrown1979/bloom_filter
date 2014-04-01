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


def testFalsePositiveRate(testSet, bloomFilter):
    length = len(testSet)
    amtTrue = 0.0
    for item in testSet:
        if bloomFilter.lookup(item):
            amtTrue += 1
    return (round(amtTrue/length, 10) * 100, amtTrue)

def reportTest(falsePos, length, memSet, testSet, m=None):
    bloomFilter = BloomFilter(c=falsePos, n=length, m=m)
    bloomFilter.addByList(memSet)
    print "amt of hashes", len(bloomFilter.hashes)
    test = testFalsePositiveRate(testSet, bloomFilter)
    print "False Positive Rate at " + str(falsePos * 100) + "% resulted in:", str(test[0]) + "%"
    print "Collisions at " + str(falsePos * 100) + "%:", test[1]

def bloomFilterDemo():
    setGenerator = DemoSetGenerator()
    membershipSet = setGenerator.membershipSet
    testSet = setGenerator.testSet
    length = len(membershipSet)

    reportTest(.01, length, membershipSet, testSet)
    reportTest(.001, length, membershipSet, testSet)
    reportTest(.0001, length, membershipSet, testSet)
    print "-------------------------------------------------------------------"
    print "Vector size of 1.5n"
    reportTest(.01, length, membershipSet, testSet, m=len(membershipSet) * 1.5)
    reportTest(.001, length, membershipSet, testSet, m=len(membershipSet) * 1.5)
    reportTest(.0001, length, membershipSet, testSet, m=len(membershipSet) * 1.5)
    print "-------------------------------------------------------------------"
    print "Vector size of .75n"
    reportTest(.01, length, membershipSet, testSet, m=len(membershipSet) * .75)
    reportTest(.001, length, membershipSet, testSet, m=len(membershipSet) * .75)
    reportTest(.0001, length, membershipSet, testSet, m=len(membershipSet) * .75)    
    print "-------------------------------------------------------------------"
    print "Vector size of .5n"
    reportTest(.01, length, membershipSet, testSet, m=len(membershipSet) * .5)
    reportTest(.001, length, membershipSet, testSet, m=len(membershipSet) * .5)
    reportTest(.0001, length, membershipSet, testSet, m=len(membershipSet) * .5)    
    print "-------------------------------------------------------------------"
    print "Random tests"
    reportTest(.01, length, membershipSet, testSet, m=450000)
    reportTest(.001, length, membershipSet, testSet, m=450000)
    reportTest(.0001, length, membershipSet, testSet, m=450000)
    print "-------------------------------------------------------------------"


bloomFilterDemo()