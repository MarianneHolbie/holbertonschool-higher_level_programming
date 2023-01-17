#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        index = 1
        if len(sys.argv) == 2:
            print("1 argument:\n{}: {}".format(index, sys.argv[index]))
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
            while index < len(sys.argv):
                print("{0}: {1}".format(index, sys.argv[index]))
                index += 1
