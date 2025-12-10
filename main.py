import arithmetic
import geometry as geo
from geometry import calc_rect_peri

print("Hello, World!")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
arithmetic.add(num1, num2)
arithmetic.subtract(num1, num2)

len = int(input("Enter Length: "))
br = int(input("Enter Breadth: "))
geo.calc_rect_area(len, br)
calc_rect_peri(len, br)
