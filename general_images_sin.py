"""
Created on Sun Mar 12 12:55:17 2017

@author: hahayi
"""

import hcindex2xy as hc
import matplotlib
import matplotlib.backends.backend_pdf as pltBack
import matplotlib.lines as lines
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from optparse import OptionParser
import os
import sys
import timeserieprocess as tsp
import timeserieprocess_matrix as tspm
import timeserieprocess_matrix_outfile as tspmo
import Multiple_Level_Snake_Hilbert as mh

rr,cc=mh.level_two(3)

t = np.arange(1024)
t = np.array(t)
#y = np.zeros((65536,), dtype=float64)
mu    = 0.0
sigma = 0.18
# Gaussian noise,mean and standard deviation
weight = 1.0
#----------------------------
prefix = "sin_noise_wei_"

i=7
for nn in xrange(1,10):
    
    y = np.sin(2.0*np.pi*t/32.0)+weight*np.random.normal(mu,sigma,len(t))
    #y= t/1024.0*3.0-1.5    
    #y = np.cos(2.0*np.pi*t/128)+weight*np.random.normal(mu,sigma,len(t))
    plt.plot(y[:60])
    filename = prefix+str(i)+'_sam_'+str(nn)
    datafile = filename+'.dat'
    headtitle = '# Sin-Function Plus Noise sigma '+str(sigma)
    np.savetxt(datafile,np.transpose([t,y]),fmt=['%g','%3.8f'], delimiter="  ",header=headtitle,comments='#time amplitude')
    
    #--------------------------------                         
    imagefile = filename+'.png'
    kk = tspmo.processFile(datafile,32,1024,0,rr,cc,imagefile)
