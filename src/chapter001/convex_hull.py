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
    return true
# checks if a point is contained in a triangle
