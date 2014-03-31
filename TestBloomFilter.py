import random
import unittest
from bloom_filter import *

class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bloomFilter = BloomFilter()
        self.smallFilter = BloomFilter(m=10)

    def test_vector_length(self):
        self.assertEqual(self.bloomFilter.vectorLength, 9593)

    def test_small_vector_length(self):
        self.assertEqual(self.smallFilter.vectorLength, 10)

    def test_num_of_hashes(self):
        self.assertEqual(self.bloomFilter.numOfHashes, 7)

    def test_small_filter_hashes(self):
        self.assertEqual(self.smallFilter.numOfHashes, 1)

    def test_num_of_hashes_fixed_m(self):
        self.assertEqual(self.bloomFilter._getNumHashesWithFixedM(9593, 1000), 7)


    # def test

class TestHashGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = HashGenerator()

    def test_that_returned_function_generates_value(self):
        self.assertLess(self.generator.generateHash(1000)(), 1001), 

if __name__ == '__main__':
    unittest.main()