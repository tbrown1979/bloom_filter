import random
import unittest
from bloom_filter_demo import *

class TestDemonstration(unittest.TestCase):

    def setUp(self):
        self.setGenerator = DemoSetGenerator()
    
    def test_correct_membership_set_size(self):
        self.assertEquals(len(self.setGenerator.membershipSet), 10000)

if __name__ == '__main__':
    unittest.main()