#!/usr/bin/env python3


def main():
    number = 1
    while True:
        tripled = triple(number)
        squared = square(number)
        if (tripled < squared):
            break
        print(f"triple({number})=={tripled} square({number})=={squared}")
        number += 1
        

def triple(number):
    return number * 3
    
def square(number):
    return number ** 2

if __name__ == "__main__":
    main()
