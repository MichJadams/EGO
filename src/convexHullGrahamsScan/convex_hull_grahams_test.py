import convex_hull_grahams
import unittest

class convex_hull_grahams_test(unittest.TestCase):
    def setUp(self):
        try:
            self.test = convex_hull_grahams.findConvexHullGrahams
            self.points = [[]]
            self.hull = []
        except NameError as e:
            pass
    # def test_returns_only_hull_points(self):
    #     expected = self.test(self.points)
    #     for point in expected:
    #         x = point[0]
    #         y = point[1]
if __name__ == '__main__':

    unittest.main()
