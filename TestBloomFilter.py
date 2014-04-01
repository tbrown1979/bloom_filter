import random
import unittest
from bloom_filter import *
from array import array

class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bloomFilter = BloomFilter()
        self.bloomFilterLength = 9593
        self.smallFilter = BloomFilter(n=5, m=10)

    def test_vector_length(self):
        self.assertEqual(self.bloomFilter.length, self.bloomFilterLength)

    def test_small_vector_length(self):
        self.assertEqual(self.smallFilter.length, 10)

    def test_num_of_hashes(self):
        self.assertEqual(self.bloomFilter.numOfHashes, 7)

    def test_small_filter_hashes(self):#2 because we take the ceil
        self.assertEqual(self.smallFilter.numOfHashes, 2)

    def test_num_of_hashes_fixed_m(self):
        self.assertEqual(self.bloomFilter._getNumHashesWithFixedM(self.bloomFilterLength, 1000), 7)

    def test_small_filter_array(self):
        self.assertEqual(self.smallFilter.bFilter, array('b', [0]*10))

    def test_large_filter_array(self):
        self.assertEqual(self.bloomFilter.bFilter, array('b', [0]*self.bloomFilterLength))

    def test_hashes_length(self):
        self.assertEqual(len(self.bloomFilter.hashes), 7)

    def test_small_filter_hashes_length(self):
        self.assertEqual(len(self.smallFilter.hashes), 2)

    def test_adding_item(self):
        self.bloomFilter.add("test")
        self.assertTrue(self.bloomFilter.bFilter.count(1),1)

    def test_looking_up_item(self):
        self.bloomFilter.add("test")
        self.assertTrue(self.bloomFilter.lookup("test"))

    # def test_hashing_item(self):
    #     self.assertEquals(self.bloomFilter._hashItem("test"), [499, 721, 821, 4285, 8380, 6476, 6847])

    def test_correct_lookups(self):
        for i in xrange(100):
            self.bloomFilter.add(i)
        for i in xrange(100):
            self.assertTrue(self.bloomFilter.lookup(i))

    def test_that_lookups_can_fail(self):
        self.assertFalse(self.bloomFilter.lookup(5))

    def test_add_list(self):
        self.bloomFilter.addByList(range(1,1001))
        self.assertEquals(self.bloomFilter.amtOfItems, 1000)

    def test_calcutlating_k_and_m(self):
        self.assertEquals(self.bloomFilter._calculateBloomFilterSettings(), (9593.0, 7))

class TestHashGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = HashGenerator()

    def test_that_returned_function_generates_value(self):
        self.assertLess(self.generator.generateHash(1000)(1), 1001), 

if __name__ == '__main__':
    unittest.main()