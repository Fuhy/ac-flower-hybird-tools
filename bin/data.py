import os
import sys


ROSE_DAT = 'rose.dat'

def acquire_rose_dat():
    ROSE = {}
    with open(os.path.join(getResourceDir(),ROSE_DAT),'r') as f:
        for line in f.readlines():
            formatLine = line.split('\t')
            print(formatLine)
            ROSE[formatLine[1]] = formatLine[7].replace('\n','')
    print(ROSE)
    return ROSE

def getResourceDir():
    current_file_path = os.path.abspath(__file__)
    return os.path.join(os.path.abspath(os.path.dirname(current_file_path) + os.path.sep + ".."), 'resource/')

