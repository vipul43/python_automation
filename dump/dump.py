import sys
import os
import time
import getpass
from collections import OrderedDict

def get_size():
    return sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))

class LRUCache:
    def __init__(self, capacity=45000):
        self.cache = OrderedDict()
        self.capacity = capacity

    def delete_temp(self):
        for root, dirs, files in os.walk('.'):
            for file in files:
                if(str(file)[0]=='.'):
                    os.remove(str(root)+"/"+str(file))

    def delete_empty(self):
        for root, dirs, files in os.walk('.'):
            for file in files:
                if(os.stat(str(root)+"/"+str(file)).st_size==0):
                    os.remove(str(root)+"/"+str(file))

    def get_file(self):
        min_time = sys.maxsize
        del_file = ""
        for root, dirs, files in os.walk('.'):
            for file in files:
                time = os.stat(str(root)+"/"+str(file)).st_mtime
                if(time<min_time):
                    min_time = time
                    del_file = str(root)+"/"+str(file)
        return del_file

    def adjust(self, size):
        self.delete_empty()
        if(size<=self.capacity):
            print("SZE_ERR: SIZE IS UNDER LIMITS")
        else:
            print("STARTING DUMP ...")
            self.delete_temp()
            while(size>self.capacity):
                file = self.get_file()
                os.remove(file)
                print("DELETED " + file)
                size = get_size()
            print("ENDING DUMP ...")

def program():
    args = getpass.getpass()
    if(args=='dumpem'):
        currdir = sys.argv[1]
        os.chdir(currdir)
        try:
            size = get_size()
            print("CURRENT DIRECTORY STORAGE IS: " + str(size))
            try:
                limit = sys.argv[2]
                L = LRUCache(limit)
            except IndexError:
                L = LRUCache()
            L.adjust(size)
            print("DUMP SUCCESSFUL")
        except OSError:
            print("SZE_ERR: ERROR IN CALCULATING SIZE OF THE DIR")
    else:
        print("PSWD_ERR: INCORRECT PASSWORD")
    

if __name__ == '__main__':
    program()