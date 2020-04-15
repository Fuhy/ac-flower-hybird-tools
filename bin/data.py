import os
import sys


ROSE_DAT = 'Roses.dat'

def acquire_rose_dat():
    ROSE = {}
    with open(os.path.join(get_resource_dir(),ROSE_DAT),'r') as f:
        for line in f.readlines():
            formatLine = line.split('\t')
            ROSE[formatLine[1]] = formatLine[7].replace('\n','')
    return ROSE

def get_resource_dir():
    current_file_path = os.path.abspath(__file__)
    return os.path.join(os.path.abspath(os.path.dirname(current_file_path) + os.path.sep + ".."), 'resource/')

