
import numpy 


class Tacka(object):
    count = 0

    def __init__(self, x, y, z): #kreira tacku za zadate koordinate
        self.id = Tacka.count
        self.x = x
        self.y = y
        self.z = z
        Tacka.count = Tacka.count + 1
        print "Tacka " + str(self.id) + " is created."

    def delete(self):     # brise objekat tacke
        print "Tacka " + str(self.id) + " deleted." 
        Tacka.count = Tacka.count - 1
        del self

    def printCoordinates(self): #stampa koordinate
        print "x=" + str(self.x)
        print "y=" + str(self.y)
        print "z=" + str(self.z)


    def getId(self):    #vraca id tacke
        return self.id

    def getNumberOfPoints(self):  #vraca ukupan broj tacaka
        return Tacka.count

