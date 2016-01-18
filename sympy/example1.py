#Osnovni primer u scypy-u
#Scypy se koristi za simbolichko programiranje matematickih izraza.
#Sto znaci da vrednosti ne moraju biti definisane pre kompjutacije,
#vec ce se primenjivati matematicke operacije nad definisanim izrazima,
#a uz pomoc supstitucije se menjaju vrednosti (u nove simbole ili konkretne vrednosti).

# Cilj ove vezbe je da pokaze razliku izmedju simbolickog(scypy modul) i nesimbolickog programiranja (math modul).

import sympy            # importuje scypy modul
import math             # importyuje math modul

xmath = math.sqrt(20)   #koren dobijen standardnom python funkcijom
xscy = sympy.sqrt(20)   #koren dobijen pomocu sympy biblioteke

print xmath  #stampa standard
print xscy   #stampa sympy
