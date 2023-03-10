import math

class Point:

    def __init__(self, *args):
        self.coords = args[0]
        self.dimension = len(self.coords)
        self.solution = False

    def __str__(self):
        return str(self.coords)

    def __repr__(self):
        return str(self.coords)

    def setSolution(self):
        self.solution = True

    def getSolution(self):
        return self.solution

    def scanNear(self, other, minDist):
        for ind in range(len(self.coords)):
            if abs(self.getCoords(ind) - other.getCoords(ind)) > minDist:
                return False
        return True

    def printSelf(self):
        return f"Point: {self.coords}"

    def getCoords(self, index) -> float:
        return self.coords[index]

    def getDimension(self) -> int:
        return self.dimension

    def distanceTo(self, otherPoint) -> float:
        if self.dimension != otherPoint.getDimension():
            raise ValueError("Dimension has to be same")
        else:
            distance = 0
            for i in range(self.dimension):
                distance += (self.getCoords(i) - otherPoint.getCoords(i)) ** 2
            return math.sqrt(distance)

    def lessThan(self, otherPoint) -> bool:
        ax_ind = 0
        while ax_ind < self.dimension and self.getCoords(
            ax_ind
        ) == otherPoint.getCoords(ax_ind):
            ax_ind += 1

        if ax_ind < self.dimension and self.getCoords(ax_ind) < otherPoint.getCoords(
            ax_ind
        ):
            return True
        else:
            return False

    def nearPivot(self, pivot, minDist):
        if abs(self.getCoords(0) - pivot.getCoords(0)) >= minDist:
            return False
        return True

    def average(self, other):
        coordinates = []
        for i in range(len(self.coords)):
            coordinates.append((self.coords[i] + other.coords[i]) / 2)
        return Point(coordinates)
