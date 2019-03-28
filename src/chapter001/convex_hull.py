def findConvexHull(arrayOfPoints):
    if len(arrayOfPoints) < 3:
        return arrayOfPoints

    memoCheckedTriangles = {}
    memoCheckPoints = {}
    externalPoints = []

    for pointOne in arrayOfPoints:

        for pointTwo in arrayOfPoints:
            if pointTwo == pointOne:
                continue

            for pointThree in arrayOfPoints:
                if pointThree == pointTwo:
                    continue
                for point in arrayOfPoints:

                    triangle = [pointOne, pointTwo, pointThree].sort()
                    if triangle not in memoCheckedTriangles:
                        memoCheckedTriangles[triangle] = True
                        if (point not in memoCheckPoints
                        and point != pointOne
                        and point != pointTwo
                        and point != pointThree):
                        #if the point is not part of the triangle being check
                        # and it has not already been checked
                        # check it
                            isContained = triangleContains(point, [pointOne,pointTwo,pointThree])
                            memoCheckPoints[point] = isContained
                        else:
                            continue
                    else:
                        continue

    for point in memoCheckPoints:
        if memoCheckPoints[point] == True:
            externalPoints.push(point)
    return externalPoints

def isContained(point, triangle):
    outerArea = findTriangleArea(triangle)
    innerArea = []
    for index in range(0,triangle):
        area = findTriangleArea(triangle[:index].append(point).append(trinalge[index:]))
        innerArea.append(area)
    if sum(innerArea) == outerArea:
        return true
    return false

def findTriangleArea(triangle):
    area = triangle[0][0](triangle[1][1] - triangle[2][1]) + triangle[1][0](triangle[2][1] - triangle[0][1]) + triangle[2][0](triangle[1][1] - triangle[0][1])
    area = abs(area)
    return area
# checks if a point is contained in a triangle
