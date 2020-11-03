import sys
import os
import time

def program():
    currdir = sys.argv[1]
    os.chdir(currdir)

if __name__ == '__main__':
    program()