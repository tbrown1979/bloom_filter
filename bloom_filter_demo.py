from sets import Set 
from random import randint

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


def fillBloomFilterWith(bloomFilter, listOfItems):
    

bloomFilterDemo()