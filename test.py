from addition import *
import unittest

class MyTest(unittest.TestCase):

	def test_addition(self):
		self.assertEqual(5,addition(4,3),"ca marche pas!!!")

if __name__ == '__main__':
    unittest.main()
  

