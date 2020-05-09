import sys
import os


def create():
    print(sys.argv)
    filename = str(sys.argv[1]) + str(sys.argv[3])
    open(filename, "a").close()
    os.system("code " + filename)

if __name__ == "__main__":
    create()