import unittest
import convex_hull

class test_convex_hull(unittest.TestCase):
    def setUp(self):
        try:
            self.test = convex_hull.findConvexHull
            self.points = [[4,2],[1,3],[4,5],[2,5],[6,4],[4,7],[2,8]]
            self.convexHullOutlinePoints = [[6,4],[4,7],[2,8],[1,3],[4,2]]
            self.containedPoints = [[4,5],[2,5]]
        except NameError as e:
            pass

    def test_creates_find_convex_hull(self):
        expected = self.test([])
        self.assertEqual(0,len(expected), msg="returns an empty array when envoked with an empty array")

    def test_less_than_three_points_passed_in(self):
        expected = self.test([[1,2],[2,2]])
        self.assertEqual(2, len(expected), 'if passed less than 3 points, returns that list')
        for point in expected:
            x = point[0]
            y = point[1]
            if x == 2 and y == 2:
                continue
            if x == 1 and y == 2:
                continue
            self.assertEqual(False, True, 'the points returns were incorrect')

    def test_passed_three_points_returns_those(self):
        expected = self.test([[1,2],[2,2],[4,5]])
        self.assertEqual(3, len(expected), 'if passed less than 4 points, returns that list')
        for point in expected:
            x = point[0]
            y = point[1]
            if x == 2 and y == 2:
                continue
            if x == 1 and y == 2:
                continue
            if x == 4 and y == 5:
                continue
            self.assertEqual(False, True, 'the points returns were incorrect')

    def test_includes_points_along_convex_hull(self):
        expected = self.test(self.points)
        for point in expected:
            x = point[0]
            y = point[1]
            if x == 6 and y == 4:
                continue
            if x == 4 and y == 7:
                continue
            if x == 2 and y == 8:
                continue
            if x == 1 and y == 3:
                continue
            if x == 4 and y == 2:
                continue
            self.assertEqual(True, False, msg="external coordinate, should be included in outline")

    def test_does_not_include_points_inside_convex_hull(self):
        expected = self.test(self.points)
        for point in expected:
            x = point[0]
            y = point[1]
            if x == 4 and y == 5:
                self.assertEqual(False, True, 'the points returns were incorrect')
            if x == 2 and y == 5:
                self.assertEqual(False, True, 'the points returns were incorrect')

class test_isContained(unittest.TestCase):
    def setUp(self):
        try:
            self.test = convex_hull.isContained
            self.point = [1,1]
            self.triangle = [[0,0],[2,0],[2,5]]
        except NameError as e:
            pass

    def test_passed_contained_point(self):
        self.assertEqual(self.test(self.point, self.triangle), True)

if __name__ == '__main__':

    unittest.main()
