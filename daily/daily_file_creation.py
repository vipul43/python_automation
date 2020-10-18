import sys
import os
from datetime import date, timedelta
import time

def fileNotFound(filename):
    for ele in os.walk("."):
        for file in ele:
            if(file==filename):
                return False
    return True

def getTodaysFileName():
    return str(date.today()) + ".md"

def copy_previous_days_contents():
    today = date.today()
    yesterday = today - timedelta(days=1)
    os.system('cp ./'+str(yesterday)+'.md ./'+str(today)+str('.md'))

def program():
    filedir = sys.argv[1]
    filename = getTodaysFileName()

    os.chdir(filedir)
    if(fileNotFound(filename)):
        os.system('touch ' + filename)
        copy_previous_days_contents()

if __name__ == '__main__':
    program()


