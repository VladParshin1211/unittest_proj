from utils import arrs
import unittest

class ArsTestCase(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get(array=[1,2,3], index= 1, default = "test"),2)
        self.assertEqual(arrs.get(array= [], index= 0, default = "test"),"test")
        self.assertEqual(arrs.get(array=[], index=100, default="test"),"test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice(coll=[1,2,3,4,5,6], start = 0, end = 2), [1,2])
        self.assertEqual(arrs.my_slice(coll=[1, 2, 3, 4, 5, 6]),[1, 2,3,4,5,6])
        self.assertEqual(arrs.my_slice(coll=[1, 2, 3, 4, 5, 6], start = 0), [1, 2, 3, 4, 5, 6])
        self.assertEqual(arrs.my_slice(coll=[1, 2, 3, 4, 5, 6], end = 100), [1, 2, 3, 4, 5, 6])
        self.assertEqual(arrs.my_slice(coll=[]), [])





