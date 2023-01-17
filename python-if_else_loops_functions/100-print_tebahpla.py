#!/usr/bin/python3
for alpha_letter in reversed(range(ord('a'), ord('z') + 1)):
    if alpha_letter % 2 != 0:
        alpha_letter -= 32
    print("{:c}".format(alpha_letter), end="")
