import unittest
import convex_hull

class test_convex_hull_test(unittest.TestCase):
    def setUp(self):
        try:
            self.test = convex_hull.findConvexHull
            self.points = [[4,2],[1,3],[4,5],[2,5],[6,4],[4,7],[2,8]]
            self.convexHullOutlinePoints = [[6,4],[4,7],[2,8],[1,3],[4,2]]
            self.containedPoints = [[4,5],[2,5]]
        except NameError as e:
            pass
    def test_creates_find_convex_hull(self):
        self.assertEqual(self.test([]),[], msg="returns an empty array when envoked with an empty array")
    def test_less_than_three_points_passed_in(self):
        self.assertEqual(self.test([[1,2],[2,2]]),[[1,2],[2,2]])
    def test_passed_three_points_returns_those(self):
        self.assertEqual(self.test([[1,2],[2,2],[4,5]]), [[1,2],[2,2],[4,5]])
    def test_includes_points_along_convex_hull(self):
        result = self.test(self.points)
        for point in self.convexHullOutlinePoints:
            self.assertIn(point, result, msg="external coordinate, should be included in outline")
    def test_does_not_include_points_inside_convex_hull(self):
        result = self.test(self.points)
        for point in self.containedPoints:
            self.assertNotIn(point, result, msg="internal coordinate, should not be included in outline")

if __name__ == '__main__':
    unittest.main()
