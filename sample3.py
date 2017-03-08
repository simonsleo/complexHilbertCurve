# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:17:25 2017

@author: sliu
"""

import hcindex2xy as hc
import matplotlib
import matplotlib.backends.backend_pdf as pltBack
import matplotlib.lines as lines
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy
from optparse import OptionParser
import os
import sys

m =3
n_cell=2**m
mm = n_cell*n_cell

n=4*n_cell

xx = numpy.zeros(n**2, dtype=numpy.int16)
yy = numpy.zeros(n**2, dtype=numpy.int16)

#------------BA----------
for j in xrange(0,3):
    y0 = -n_cell*j
    
    for i in xrange(0, mm):
        ii = i+j*mm
        xx[ii],yy[ii] =hc.hcindex2xy_ba(n_cell,i)
        yy[ii]+=y0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
#----------BC-------------
for j in xrange(0,4):  
    y0 = -3*n_cell
    x0 = n_cell*j                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    for i in xrange(0, mm):
        ii = i+(3+j)*mm
        xx[ii],yy[ii] =hc.hcindex2xy_bc(n_cell,i)
        xx[ii] +=x0
        yy[ii] +=y0
        
#----------DC-------------
for j in xrange(0,2):
    x0 = 4*n_cell-1
    y0 = -3.0*n_cell+1+j*n_cell
    for i in xrange(0, mm):
        ii = i+(7+j)*mm
        xx[ii],yy[ii] =hc.hcindex2xy_dc(n_cell,i)
        xx[ii] +=x0
        yy[ii] +=y0
        
        
#----------DA-------------
for j in xrange(0,3):
    x0 = (4-j)*n_cell-1
    y0 = -n_cell+1
    for i in xrange(0, mm):
        ii =i+(9+j)*mm
        xx[ii],yy[ii] =hc.hcindex2xy_da(n_cell,i)
        yy[ii] +=y0
        xx[ii] +=x0


#------------BA----------
for j in xrange(0,1):
    y0 = -n_cell*(j+1)
    x0 = n_cell
    
    for i in xrange(0, mm):
        ii = i+(12+j)*mm
        xx[ii],yy[ii] =hc.hcindex2xy_ba(n_cell,i)
        yy[ii]+=y0
        xx[ii]+=x0
     

#----------BC-------------
for j in xrange(0,2):  
    y0 = -2*n_cell
    x0 = n_cell*(j+1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    for i in xrange(0, mm):
        ii = i+(13+j)*mm
        xx[ii],yy[ii] =hc.hcindex2xy_bc(n_cell,i)
        xx[ii] +=x0
        yy[ii] +=y0
                
                
 #----------DA-------------
for j in xrange(0,1):
    x0 = (3-j)*n_cell-1
    y0 = -2*n_cell+1
    for i in xrange(0, mm):
        ii =i+(15+j)*mm
        xx[ii],yy[ii] =hc.hcindex2xy_da(n_cell,i)
        yy[ii] +=y0
        xx[ii] +=x0
        
                     

       
plt.plot(xx, yy)
plt.title('HilbertCurve_sample3')
v = [numpy.min(xx)-2, numpy.max(xx)+2,numpy.min(yy)-1,numpy.max(yy)+1]
plt.axis(v)
plt.show()
#image = numpy.zeros((n,n))
#plt.pcolor(distance)
#plt.colorbar() 