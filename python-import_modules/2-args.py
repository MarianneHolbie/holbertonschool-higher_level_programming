#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 argument.")
    else:
        index = 1
        print("{} arguments:".format(len(sys.argv) - 1))
        while index < len(sys.argv):
            print("{0}: {1}".format(index, sys.argv[index]))
            index += 1
