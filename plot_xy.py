import numpy as np
from pyMCDS import pyMCDS

# dir='output_1sec/'
dir='output_1cell/'

for idx in range(5):
    fname = f'output{idx:08d}.xml'
    mcds = pyMCDS(fname, dir, microenv=False, graph=False, verbose=False)
    xvals = mcds.data['discrete_cells']['data']['position_x']
    yvals = mcds.data['discrete_cells']['data']['position_y']
    #print("len(xvals) = ",len(xvals))
    print(f't={mcds.get_time()}: x,y= {xvals[0]},{yvals[0]}')

# xml_file="output00000001.xml"
# mcds = pyMCDS(xml_file, dir, microenv=False, graph=False, verbose=True)
# xvals = mcds.data['discrete_cells']['data']['position_x']
# yvals = mcds.data['discrete_cells']['data']['position_y']
# #print("len(xvals) = ",len(xvals))
# print("t = ",mcds.get_time())
# print("xvals[0] = ",xvals[0])

#zvals = mcds.data['discrete_cells']['data']['position_z']
#xv = xvals[0]         
#yv = yvals[0]
#zv = zvals[idx]
#print("len(xvals) 
