import sys
import os

filename = sys.argv[1]
filedir = sys.argv[2]

os.chdir(filedir)
os.system('touch ' + filename)

os.chdir('/Users/vipul/Documents/coding/cp')
file, extension = filename.split('.')
if(extension=="py"):
    cp_file_path = './cp_python_template.py'
elif(extension=="cpp"):
    cp_file_path = './cp_cpp_template.cpp'
os.system('cp ' + cp_file_path + ' ../../../../..' + filedir + '/' + filename)