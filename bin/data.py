import os
import sys
import flower

ROSES_DAT_NAME = 'Roses.dat'
COSMOS_DAT_NAME = 'Cosmos.dat'
HYACINTHS_DAT_NAME = 'Hyacinths.dat'
LILIES_DAT_NAME = 'Lilies.dat'
MUMS_DAT_NAME  = 'Mums.dat'
PANSIES_DAT_NAME  = 'Pansies.dat'
TULIPS_DAT_NAME  = 'Tulips.dat'
WINDFLOWERS_DAT_NAME  = 'Windflowers.dat'

def acquire_dat(data_file_name):
    DAT = {}
    with open(os.path.join(get_resource_dir(),data_file_name),'r') as f:
        for line in f.readlines():
            formatLine = line.split('\t')
            DAT[formatLine[1]] = formatLine[len(formatLine)-1].replace('\n','')
    return DAT

def get_resource_dir():
    current_file_path = os.path.abspath(__file__)
    return os.path.join(os.path.abspath(os.path.dirname(current_file_path) + os.path.sep + ".."), 'resource/')

def _data_init():
    return {
        flower.FLOWER_KIND['Roses'] :  acquire_dat(ROSES_DAT_NAME),
        flower.FLOWER_KIND['Cosmos'] :  acquire_dat(COSMOS_DAT_NAME),
        flower.FLOWER_KIND['Hyacinths'] :  acquire_dat(HYACINTHS_DAT_NAME),
        flower.FLOWER_KIND['Lilies'] :  acquire_dat(LILIES_DAT_NAME),
        flower.FLOWER_KIND['Mums'] :  acquire_dat(MUMS_DAT_NAME),
        flower.FLOWER_KIND['Pansies'] :  acquire_dat(PANSIES_DAT_NAME),
        flower.FLOWER_KIND['Tulips'] :  acquire_dat(TULIPS_DAT_NAME),
        flower.FLOWER_KIND['Windflowers'] :  acquire_dat(WINDFLOWERS_DAT_NAME),
    }
    

FLOWER_GENE_DAT = _data_init()