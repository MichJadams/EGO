class convexHullNaive():
    def __init__(self):
        #a list of all the points already checked as being internal to some triangle
        self.memoCheckPoints = {}
        #a list of all the already checked triangles
        self.memoCheckedTriangles = {}
        #the external points returned at the end
        self.externalPoints = []
        self.boolean = False

    def findConvexHull(self,arrayOfPoints):
        #a list of all the points already checked as being internal to some triangle
        self.memoCheckPoints = {}
        #a list of all the already checked triangles
        self.memoCheckedTriangles = {}
        #the external points returned at the end
        self.externalPoints = []
        if len(arrayOfPoints) <= 3:
            return arrayOfPoints
        for pointOne in arrayOfPoints:
            for pointTwo in arrayOfPoints:
                if pointTwo == pointOne:
                    continue

                for pointThree in arrayOfPoints:
                    if pointThree == pointTwo or pointThree == pointOne:
                        continue
                    triangle = [pointOne, pointTwo, pointThree]
                    triangle.sort()
                    if str(triangle) not in self.memoCheckedTriangles:
                        self.memoCheckedTriangles[str(triangle)] = True

                    for point in arrayOfPoints:
                        # if str(point) not in self.memoCheckPoints:
                        if str(point) in self.memoCheckPoints and self.memoCheckPoints[str(point)] == True:
                                    continue
                        if point != pointOne:
                            if point != pointTwo:
                                if point != pointThree:
                                #if the point is not part of the triangle being check
                                # and it has not already been checked
                                # check it
                                    isContained = self.isContained(point, [pointOne,pointTwo,pointThree])
                                    self.memoCheckPoints[str(point)] = isContained

        for point in self.memoCheckPoints:
          if self.memoCheckPoints[point] == False:
              x = int(point[1])
              y = int(point[4])
              point = [x,y]
              self.externalPoints.append(point)
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
        areaThree =  triangle[2][0]*(triangle[0][1] - triangle[1][1])

        area = abs((area + areaOne + areaThree)/2)
        return area
# checks if a point is contained in a triangle
