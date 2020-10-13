import sys
import os
from datetime import date
import time

def fileNotFound(filename):
    for ele in os.walk("."):
        for file in ele:
            if(file==filename):
                return False
    return True

def getTodaysFileName():
    return str(date.today()) + ".md"

def program():
    filedir = sys.argv[1]
    filename = getTodaysFileName()

    os.chdir(filedir)
    if(fileNotFound(filename)):
        os.system('touch ' + filename)

if __name__ == '__main__':
    program()


