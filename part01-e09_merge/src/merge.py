#!/usr/bin/env python3

def merge(L1, L2):
    list1 = L1.copy()
    list2 = L2.copy()
    list3 = []
    while list1 and list2:
        if list1[0] < list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))
    list3.extend(list1 or list2)
    return list3

def main():
    #debugging code
    list4 = [1, 2, 3, 4, 5]
    list5 = [6, 7, 8, 9, 10]
    print(merge([1, 3, 5], [2, 4, 6]))
    print(len(list4) + len(list5))

if __name__ == "__main__":
    main()
