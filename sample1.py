# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:27:54 2017

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

m=3
n_cell=2**m
mm = n_cell*n_cell

n=2**(m+1)

xx = numpy.zeros(n**2, dtype=numpy.int16)
yy = numpy.zeros(n**2, dtype=numpy.int16)

#------------BA----------
for i in xrange(0, mm):
       xx[i],yy[i] =hc.hcindex2xy_ba(n_cell,i)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
#----------BD-------------
for i in xrange(0, mm):
       ii = i+mm
       xx[ii],yy[ii] =hc.hcindex2xy_bd(n_cell,i)
       yy[ii] +=(-n_cell)
        
#----------AC-------------
for i in xrange(0, mm):
       ii = i+2*mm
       xx[ii],yy[ii] =hc.hcindex2xy_ac(n_cell,i)
       yy[ii] +=(-2*n_cell+1)
       xx[ii] +=n_cell
#----------DA-------------
for i in xrange(0, mm):
       ii =i+3*mm
       xx[ii],yy[ii] =hc.hcindex2xy_da(n_cell,i)
       yy[ii] +=(-n_cell+1)
       xx[ii] +=2*n_cell-1
plt.plot(xx, yy)
plt.title('HilbertCurve_sample1')
v = [numpy.min(xx)-2, numpy.max(xx)+2,numpy.min(yy)-1,numpy.max(yy)+1]
plt.axis(v)
#image = numpy.zeros((n,n))
#plt.pcolor(distance)
#plt.colorbar() 
plt.show()

plt.subplot(221)
plt.plot(xx[:mm],yy[:mm])
plt.axis(v)

plt.subplot(223)
plt.plot(xx[mm-1:2*mm],yy[mm-1:2*mm])
plt.axis(v)


plt.subplot(224)
plt.plot(xx[2*mm:3*mm],yy[2*mm:3*mm])
plt.axis(v)


plt.subplot(222)
plt.plot(xx[3*mm:4*mm],yy[3*mm:4*mm])
plt.axis(v)





