class convexHullNaive():
    def __init__(self):
        self.memoCheckPoints = {}
        self.memoCheckedTriangles = {}
        self.externalPoints = []

    def findConvexHull(self,arrayOfPoints):
        if len(arrayOfPoints) <= 3:
            return arrayOfPoints

        for pointOne in arrayOfPoints:
            for pointTwo in arrayOfPoints:
                if pointTwo == pointOne:
                    continue
                for pointThree in arrayOfPoints:
                    if pointThree == pointTwo:
                        continue
                    for point in arrayOfPoints:
                        triangle = [pointOne, pointTwo, pointThree].sort()
                        if triangle not in self.memoCheckedTriangles:
                            self.memoCheckedTriangles[triangle] = True
                            pointHash = str(point)
                            if (pointHash not in self.memoCheckPoints
                            and point != pointOne
                            and point != pointTwo
                            and point != pointThree):
                            #if the point is not part of the triangle being check
                            # and it has not already been checked
                            # check it
                                isContained = self.isContained(point, [pointOne,pointTwo,pointThree])
                                self.memoCheckPoints[pointHash] = isContained
                            else:
                                continue
                        else:
                            continue

        for point in self.memoCheckPoints:
            if self.memoCheckPoints[point] == True:
                self.externalPoints.push(point)
        return self.externalPoints

    def isContained(self, point, triangle):
        outerArea = self.findTriangleArea(triangle)
        innerArea = []
        for localpoint in triangle:
            thisTriangle = [e if e is not localpoint else point for e in triangle ]
            area = self.findTriangleArea(thisTriangle)
            innerArea.append(area)
        if sum(innerArea) == outerArea:
            return True
        return False

    def findTriangleArea(self,triangle):
        area = triangle[0][0]*(triangle[1][1] - triangle[2][1])
        areaOne = triangle[1][0]*(triangle[2][1] - triangle[0][1])
        areaThree =  triangle[2][0]*(triangle[1][1] - triangle[0][1])

        area = abs(area + areaOne + areaThree)
        return area
# checks if a point is contained in a triangle
