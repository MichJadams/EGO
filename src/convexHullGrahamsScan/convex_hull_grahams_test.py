import convex_hull_grahams
import unittest

class convex_hull_grahams_test(unittest.TestCase):
    def setUp(self):
        try:
            self.testClass = convex_hull_grahams.ConvexHullGrahams()
        except NameError as e:
            pass
    def test_passed_empty_array_returns(self):
        expected = self.testClass.findConvexHullGrahams([])
        self.assertEqual(len(expected), 0)
    def test_passed_less_than_three_points_returns_all(self):
        expected = self.testClass.findConvexHullGrahams([[1,2]])
        for point in expected:
            x = point[0]
            y = point[1]
    def test_passed_less_than_three_points_returns_all(self):
        expected = self.testClass.findConvexHullGrahams([[1,2]])
        for point in expected:
            x = point[0]
            y = point[1]
if __name__ == '__main__':
    unittest.main()
