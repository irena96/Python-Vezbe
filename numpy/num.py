import numpy

niz = numpy.array([[1,2,3,4,5],[2,3,4,5,6]])

niz_gen = numpy.arange(0.0,1000000.)
niz_gen2 = numpy.arange(1000000.,2000000.)

#print niz_gen2
niz3 = niz_gen2.copy()
#print niz3
niz4 = numpy.empty([2,3])
#print niz4

niz5 = numpy.empty_like(niz4)
#print niz5


jed_matrica = numpy.eye(100,k=1)
#print jed_matrica

fileM = open('matrix', 'rw')
#print fileM
matFromFile = numpy.fromfile(fileM, sep="\n")
#print matFromFile

file2 = open("izKodaSnimljeno.mat", 'r')
#numpy.save(file2, matFromFile)

matFromBinary = numpy.load(file2)
x = matFromBinary.reshape((12,3))

#print matFromBinary
print x

print numpy.amax(x, axis=0)
print numpy.amin(x, axis=0)
print numpy.amax(x, axis=1)
print numpy.amin(x, axis=1)

print numpy.array_split(x, 3)[0]

print numpy.sort(x[0], axis=0)

print numpy.cumsum(numpy.array_split(x, 3)[0])
print numpy.array_split(x, 3)[0].sum()

#print niz_gen
#print niz_gen2
#
#print niz_gen.dtype
#
#print niz_gen + niz_gen2
#
