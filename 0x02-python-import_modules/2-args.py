#/usr/bin/python3

if __name__ = "__main__":
    import sys

    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i + 1]))

