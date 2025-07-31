#!/usr/bin/env python3

def detect_ranges(L):
    if not L:
        return []

    sorted_list = sorted(L)
    result = []

    start = sorted_list[0]

    for prev, curr in zip(sorted_list, sorted_list[1:]):
        if curr != prev + 1:
            if start == prev:
                result.append(start)
            else:
                result.append((start, prev + 1))
            start = curr

    # Handle the last element or range
    if start == sorted_list[-1]:
        result.append(start)
    else:
        result.append((start, sorted_list[-1] + 1))

    return result
        
    

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
