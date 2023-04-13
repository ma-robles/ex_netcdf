from netCDF4 import Dataset
import numpy as np

from sys import argv

filename = argv[1]
print(filename)
root=Dataset(filename, 'r')
print('Tipo de NetCDF:',root.file_format)
print('Dimensiones:', root.dimensions)
for k in root.dimensions.keys():
    dim=root.dimensions[k]
    print('\t',dim.name,':',dim.size)
claves=root.variables.keys()
print(claves)
