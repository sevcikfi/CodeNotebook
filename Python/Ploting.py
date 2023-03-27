import matplotlib.pyplot as plt
import math                             # Používáme goniometrické funkce

# plt.ion()                             # Interactive Mode On - pokud spustíme tuto funkci, program nebude zastavovat na plt.show()

xs = [0.1 * i for i in range(100)]      # Hodnoty x od 0 do 10 s krokem 0.1
ys1 = [math.sin(x) for x in xs]         # Funkce sin(x)

plt.plot(xs, ys1)                       # Vykreslení grafu
plt.show()                              # Zobrazení grafu


""" Více grafů v jednom panelu """
ys2 = [math.tan(x) for x in xs]         # Funkce tangens

plt.plot(xs, ys1)
plt.plot(xs, ys2)
#plt.show()                              # Ukáže graf. POZOR, Pro pokračování provádění kódu je potřeba graf zavřít (pokud nepoužíváte interaktivní mód plt.ion())

""" Popisky os a grafu"""
plt.clf()
plt.plot(xs, ys1, color="red", linestyle=":", label="$\\sin(x)$")
plt.plot(xs, ys2, "b-.", label="$\\tan(x)$")
plt.xlabel("$x$")                       # Popisky os (lze použít příkazy LaTeXu uvozené znaky $$)
plt.ylabel("$y$")
plt.title("Goniometrie")                # Popisek grafu
plt.ylim(-3, 3)                         # Meze osy y
plt.legend()                            # Zobrazí legendu
#plt.savefig("d:\\obrazek.pdf")          # Uloží obrázek do souboru
#plt.savefig("obrazek.pdf")          # Uloží obrázek do souboru
#plt.show()

""" Více panelů """
plt.clf()
plt.subplot(211)                        # Číslo vyjadřuje počet řádků, počet sloupců a pořadí grafu
plt.plot(xs, ys1)
plt.xlabel("$x$")
plt.ylabel("$\\sin(x)$")

plt.subplot(212)
plt.plot(xs, ys2, color="red", linewidth=3.0)
plt.xlabel("$x$")
plt.ylabel("$\\tan(x)$")
plt.ylim(-3, 3)

plt.suptitle("Goniometrie")             # Hlavní nadpis celého grafu
#plt.show()
#plt.savefig("multiple-panels.jpg")
plt.clf()

####################################################
## Contour - colour maps
####################################################

#import matplotlib.pyplot as plt
from matplotlib import cm               # Colour maps for the contour graph
import numpy as np

def f(x, y):                            # Example of a function of two independent variables
    return x**4 - 2*x**2 + x + y**2

numSteps = 100                          # Number of points in the mesh
numContours = 30                        # Number of contours in the graph

x = y = np.linspace(-2.0, 2.0, numSteps)# Range of x and y values for the graph

X, Y = np.meshgrid(x, y)                # Grid for calculating values of the function
Z = f(X, Y)                             # numpy is powerful and can handle this

# cmap specifies one of the colour map. All colour maps are given in
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
plt.contourf(X, Y, Z, numContours, cmap=cm.hot) # type: ignore
plt.colorbar()                          # Legend for the contour graph
#plt.show()
#plt.savefig("contour.jpg")