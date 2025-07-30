#!/usr/bin/env python3

import math

def triangle_area():
    base = input("Give the base of the triangle: ")
    height = input("Give the height of the triangle: ")
    print("The area is {:6f}".format(0.5 * float(base) * float(height)))

def rectangle_area():
    width = input("Give the width of the rectangle: ")
    height = input("Give the height of the rectangle: ")
    print("The area is {:6f}".format(float(width) * float(height)))

def circle_area():
    radius = input("Give the radius of the circle: ")
    print("The area is {:6f}".format(math.pi * float(radius) ** 2))

def main():
    while True:
        shape = input("What shape do you want to calculate the area for? (triangle/rectangle/circle/exit): ").strip().lower()
        if shape == "triangle":
            triangle_area()
        elif shape == "rectangle":
            rectangle_area()
        elif shape == "circle":
            circle_area()
        elif shape == "":
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
