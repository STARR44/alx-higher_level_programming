#!/usr/bin/python3
for b in range(97, 123):
    if b in [113, 101]:
        continue
    print(f"{chr(b)}", end="")
