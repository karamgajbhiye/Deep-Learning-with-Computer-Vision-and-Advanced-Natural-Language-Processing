'''3. Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3'''

import math
print('Volume of a Sphere')
print('Enter the diameter of sphere:')
diameter = int(input())
r = diameter/2

#pi = 3.14

V = (4/3) * (math.pi) * (r**3)

print('volume of a sphere with diameter {} cm is {} cm3.'.format(diameter,V))