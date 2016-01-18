# Ovaj primer ima za cilj da pokaze kako se definisu simboli i izrazi,
# i kako se vrsi zamena simbola drugim simbolom ili izrazom ili skalarom (konkretna vrednost).

import sympy as sp            # imoprt sympy modula  

delimiter = 30 * "-" # definicija separatora redova ... buahahahha
#definicija simbola 
x = sp.symbols("x")  # definicija simbola x
y = sp.symbols("y")  # definicija simbola y

p, k, r = sp.symbols("p k r") # definicija simbola p, k (nacin2)

print delimiter
print  "Ovo su nasi simboli: "
print x, y, p, k, r
print delimiter

#definicija izraza:
izraz1 = 2*x**2 + 3*y + 6
izraz2 = 5*x**3 + 7*y**2 + 2

print "Ovo su nasi izrazi:"
print izraz1
print izraz2
print delimiter

#definicija zamena: (nacin1)
print "Ovo su nase zamene:"
zamena1 = (x, 5)
zamena2 = (y, 3)

vrednost1 = izraz1.subs([zamena1, zamena2])
print "Vrednost izraza1:"
print vrednost1
print delimiter

vrednost2 = izraz2.subs([zamena1, zamena2])
print "Vrednost izraza2:"
print vrednost2
print delimiter

#definicija zamena: (nacin2)
vrednost1 = izraz1.subs([(x,5),(y,3)])
vrednost2 = izraz2.subs([(x,5),(y,3)])
print "Nasi izrazi 1 i 2 imaju vrednosti:"
print vrednost1, vrednost2
print delimiter


#zamena simbola drugim simbolom:
vrednost3 = izraz1.subs([(x, 5),(y, x)])
print vrednost3
print delimiter
#redosled zamene 2
vrednost4 = izraz1.subs([(y, x), (x, 5)])
print vrednost4
print delimiter

