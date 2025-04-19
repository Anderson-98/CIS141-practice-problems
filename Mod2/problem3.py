'''# 3. Create a program that prompts for the side lengths of 
a triangle and computes the area using Heron's formula.'''

import math

# prompt the user for three side lengths
a = int(input("enter side length a:"))
b = int(input("enter side length b:"))
c = int(input("enter side length c:"))

# Compute the semi-perimeter
s = (a + b + c) / 2

# Compute the value inside sqrt
value_inside_sqrt = s * (s - a) * (s - b) * (s - c)

# Compute the area only if the value inside sqrt is non-negative
area = math.sqrt(abs(value_inside_sqrt)) 

print(f"the area of the triangle is: {area:.2f}")
