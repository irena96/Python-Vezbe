import matplotlib.pyplot as pplot
import numpy

from Tacka import Tacka
from Linija import Linija
from Krug import Krug

o = Tacka( 0, 0, 0)
t1 = Tacka(-5,9,1)
t2 = Tacka(7,-3,2)

#o.delete()
#t1.delete()
#t2.delete()

#print o.getNumberOfPoints()
#t1.printCoordinates()
#o.printCoordinates()

linija1 = Linija(t1, t2)
x1 = linija1.getSolutionForXY(1.5)

xs = numpy.arange(0,50,1)
ys = []
for each in xs:
    y = float(linija1.getSolutionForXY(each))
    ys.append(y)

krug1 = Krug(o, 1)

krugY = []

for each in xs:
    print krug1.getSolutionForXY(each)
#    y = float(krug1.getSolutionForXY(each))
#    krugY.append(y)

print krugY

print krug1.getSolutionForXY(1)

pplot.plot(xs, ys, "k.")
pplot.plot(xs, krugY, "r.")
pplot.show()


