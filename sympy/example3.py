#Ovo je vezba 3
#Irena, ovo je ok.

#Ova vezba ima za cilj da pokaze promenu matematickog izraza iz stringa u sympy izraz. 
#Takodje pokazuje postupak prebacivanja iz izraza u pravu vrednost za funkcije koje nemaju
#u sebi simbole. (ex: sympy.sqrt(17))
#Note: pokazan je i primer koriscenja try, except kljucnih reci u pythonu. (see also: finally)

import sympy

# potrebna je explicitna deklaracija simbola, kao u example2.py
x, y = sympy.symbols("x, y")
izraz_string = "x**2 + 2*y + 1"  # definicija izraza kao string (moze da se cita iz fajla)

izraz = sympy.sympify(izraz_string)
#izraz_string = sympy.sympify(izraz_string)  #prepisivanje izraz_string u tip expr

try:
    # ovde se vrsi pokusaj red po red
    print z
    res = izraz_string.subs([(x,3), (y,5)])
    print "Izraz ima oblik:" , res
    #ma gde da kod ima gresku izvrsava se except blok
except:
    #ovo se izvrsava ukoliko ima gresaka u try bloku
    print "Izraz je tipa: " + str(type(izraz_string)) + ". Scypy ga ne prepoznaje kao izraz."

try:
    res = izraz.subs([(x, 3), (y,5)])
    print "Izraz ima oblik:" , res
except:
    print "Izraz je tipa: " + str(type(izraz)) + ". Scypy ga ne prepoznaje kao izraz."


#evaluacija izraza ('procena' prave vrednosti):
koren = sympy.sqrt(20)
print "symbolic:"
print koren/10           # nastavlja da 'vozi' sympy expr
print "eval:"
print koren.evalf()/10   # vraca pravu vrednost korena
