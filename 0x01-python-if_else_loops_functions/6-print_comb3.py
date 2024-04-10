#!/usr/bin/python3
for p in range(0, 10):
    for q in range(p + 1, 10):
        if p == 8 and q == 9:
            print("{}{}" .format(p, q))
        else:
            print("{}{}" .format(p, q), end=", ")
