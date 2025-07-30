#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    return (root1, root2)


def main():
    pass

if __name__ == "__main__":
    main()
