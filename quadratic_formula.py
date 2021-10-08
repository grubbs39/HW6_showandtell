import math
import quadratic_formula_functions

print("input a, b, and c for the quadratic formula: ")
input_line = input()
split_line = input_line.split(" ")
a = float(split_line[0])
b = float(split_line[1])
c = float(split_line[2])
solution = quadratic_formula_functions.quadratic_formula(a, b, c)
print("Solutions to {:.0f}x^2 + {:.0f}x + {:.0f} = 0".format(a, b, c))
quadratic_formula_functions.print_number(solution[0], "x1 = ")
quadratic_formula_functions.print_number(solution[1], "x2 = ")
