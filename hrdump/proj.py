import sys
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def program():
    currdir = sys.argv[1]
    os.chdir(currdir)

if __name__ == '__main__':
    program()