import unittest
import convex_hull

class convex_hull_test(unittest.TestCase):
    def setUp(self):
        try:
            self.testClass = convex_hull.convexHullNaive()
            self.points = [[4,2],[1,3],[4,5],[2,5],[6,4],[4,7],[2,8]]
            self.convexHullOutlinePoints = [[6,4],[4,7],[2,8],[1,3],[4,2]]
            self.containedPoints = [[4,5],[2,5]]
        except NameError as e:
            pass

    def test_creates_find_convex_hull(self):
        expected = self.testClass.findConvexHull([])

        self.assertEqual(0,len(expected), msg="returns an empty array when envoked with an empty array")

    def test_less_than_three_points_passed_in(self):
        expected = self.testClass.findConvexHull([[1,2],[2,2]])

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
        expected = self.testClass.findConvexHull([[1,2],[2,2],[4,5]])

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
        self.testClass = convex_hull.convexHullNaive()
        expected = self.testClass.findConvexHull([[4,2],[1,3],[4,5],[2,5],[6,4],[4,7],[2,8]])

        self.assertEqual(7, len(self.testClass.memoCheckPoints.keys()))
        self.assertEqual(5, len(expected), 'if passed less than 4 points, returns that list')
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
            error = '{0},{1} is internal and should not have been included'.format(x,y)
            self.assertEqual(True, False, msg=error)

    def test_does_not_include_points_inside_convex_hull(self):
        expected = self.testClass.findConvexHull(self.points)
        for point in expected:
            x = point[0]
            y = point[1]
            if x == 4 and y == 5:
                error = '{0},{1} is internal and should not have been included'.format(x,y)
                self.assertEqual(False, True, msg=error)
            if x == 2 and y == 5:
                self.assertEqual(False, True, 'the points returns were incorrect')

    def test_isContained_true(self):
        self.assertEqual(self.testClass.isContained([1,1],[[0,0],[2,0],[2,5]]), True)
    def test_isContained_secondCoords_true(self):
        self.assertEqual(self.testClass.isContained([4,3],[[1,3],[4,2],[6,4]]), True)

if __name__ == '__main__':
    unittest.main()
