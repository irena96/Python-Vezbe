import numpy
import sympy 

class Linija(object):
    def __init__(self, tacka1, tacka2):
        a, b = sympy.symbols("a b")
        jedn1 = a*tacka1.x + b - tacka1.y 
        jedn2 = a*tacka2.x + b - tacka2.y
         
        resenje1 = sympy.solve(jedn1, b)

        a1 = sympy.solve(resenje1, a)
        a1 = a1.get(a)

        b1 = jedn2.subs('a', a1)
        b1 = sympy.solve(b1, b)[0]

        self.x, self.y = sympy.symbols('x y')
        self.prava = a1*self.x + b1 - self.y


    def getSolutionForXY(self, newX):
        resenjeJed = self.prava.subs('x', newX )
        newY = sympy.solve(resenjeJed, self.y)
        return newY[0]

        #print a1
        #print b1


#        print jedn1
#        print jedn2
