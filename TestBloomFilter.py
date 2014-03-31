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
        self.assertEqual(self.bloomFilter.vectorLength, self.bloomFilterLength)

    def test_small_vector_length(self):
        self.assertEqual(self.smallFilter.vectorLength, 10)

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
    # def test

class TestHashGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = HashGenerator()

    def test_that_returned_function_generates_value(self):
        self.assertLess(self.generator.generateHash(1000)(1), 1001), 

if __name__ == '__main__':
    unittest.main()