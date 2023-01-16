#!/usr/bin/python3
for alpha_letter in range(ord('a'), ord('z') + 1):
    letter = chr(alpha_letter)
    if letter not in 'qe':
        print("{:c}".format(alpha_letter), end="")
