import datetime
import numpy as np
#2007
rendimientos = [
    18.0, 
    18.0 ,
    16.0,
    10.0 ,
    10.0,
    16.0,
    16.0,
    16.0 
]

porcent = [
    0.07,
    0.03,
    0.02,
    0.04,
    0.06,
    0.09,
    0.15,
    0.12,
    0.06,
    0.08,
    0.13,
    0.15 ,
]
cosechas = [
    0.082,
    0.117,
    0.106,
    0.095,
    0.087,
    0.074,
    0.053,
    0.057,
    0.073,
    0.090,
    0.076,
    0.083,
]


dt = []
for rend in rendimientos:

    for por in cosechas:
        
        mensual_r = rend*por
        dt.append( mensual_r )
        print str( mensual_r )
    



