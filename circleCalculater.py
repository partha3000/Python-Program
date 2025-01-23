"""
Exprement Number : 04
Expreiment Name :  write a py program that calculates the area of a circle based on the radios
"""

# Import the 'pi' constant from the 'math' module to calculate  the area of a circle
from math import pi

# Prompt the user to input the radius of the circle
r = float(input("Input the radius of the circle :"))

# Calculate the area of the circle using the formula : area = r.
area = pi * r ** 2

#Display the result, including the radius and calculate area.
print("The area of the circle with radius " + str(r) + "is :" + str(area))