import numpy
import sympy

class Krug(object):
    def __init__(self, centar, poluprecnik):
        self.poluprecnik = poluprecnik

        self.x, self.y, self.r = sympy.symbols('x y r')
        self.jedn = (self.x - centar.x)**2 + (self.y - centar.y) **2 - self.r**2

    def getSolutionForXY(self, newX):
        newY = self.jedn.subs([('x', newX), ('r', self.poluprecnik)])
        y = sympy.solve(newY, self.y)

        if type(y) == 'list':
            return y[0]
        else:
            return y
