#!/usr/bin/env python3

def interleave(*lists):
    #print(lists)
    temp = list(zip(*lists))
    print(temp)
    list1 = []
    for i in temp:
        for j in i:
            list1.append(j)
    print(list1)
    return list1

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
