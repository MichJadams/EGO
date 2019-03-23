import unittest
import convex_hull

print("running tests")

class test_convex_hull_test(unittest.TestCase):
    def test_setUp(self):
        try:
            self.test = convex_hull.findConvexHull()
        except NameError as e:
            pass
    def test_creates_find_convex_hull(self):
        self.assertEqual(self.test([]),[])

if __name__ == '__main__':
    unittest.main()
