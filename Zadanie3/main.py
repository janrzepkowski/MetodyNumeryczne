from funkcje import print_function
from interpolacja import equidistant_nodes, interpolation_coefficients, interpolation_value
from wykresy import gen_chart
import numpy as np

# wybierz funkcję
fun_name, fun_ptr = print_function()

# pobierz dane
a = float(input("Podaj lewą stronę przedziału: "))
b = float(input("Podaj prawą stronę przedziału: "))
points_am = int(input("Podaj ile węzłów wygenerować: "))

# ustaw dobrze początek i koniec przedziału
if a > b: a, b = b, a

# pobierz nazwę pliku
filename = "wykresy/" + input("Podaj nazwę pliku z wykresem: ")

# generowanie interpolacji z punktami równoodległymi
points_eq = []
for x in equidistant_nodes(a, b, points_am):
    points_eq.append([x, fun_ptr(x)])
points_eq = np.array(points_eq).transpose()

node_x = points_eq[0]
node_y = points_eq[1]
interpol_coef, h = interpolation_coefficients(node_x, node_y)
gen_chart(fun_ptr, lambda x: interpolation_value(node_x, interpol_coef, h, x), points_eq, a, b, filename + ".png")

print("funkcja:       {}".format(fun_name))
print("przedział:     {} - {}".format(a, b))
print("liczba węzłów: {}".format(points_am))
print()
print("interpolacja Newtona dla węzłów równoodległych :")
print("    współczynniki:   {}".format(interpol_coef))
print("    węzły (x):       {}".format([round(elem, 3) for elem in points_eq[0]]))
print("    węzły (y):       {}".format([round(elem, 3) for elem in points_eq[1]]))
