# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:29:23 2017

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

n=3*n_cell

xx = numpy.zeros(n**2, dtype=numpy.int16)
yy = numpy.zeros(n**2, dtype=numpy.int16)

#------------AD----------
for i in xrange(0, mm):
       xx[i],yy[i] =hc.hcindex2xy_ad(n_cell,i)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
#----------AD-------------
for i in xrange(0, mm):
       ii = i+mm
       xx[ii],yy[ii] =hc.hcindex2xy_ad(n_cell,i)
       xx[ii] +=n_cell
        
#----------AD-------------
for i in xrange(0, mm):
       ii = i+2*mm
       xx[ii],yy[ii] =hc.hcindex2xy_ad(n_cell,i)
       xx[ii] +=2*n_cell
#----------CD-------------
for i in xrange(0, mm):
       ii =i+3*mm
       xx[ii],yy[ii] =hc.hcindex2xy_cd(n_cell,i)
       yy[ii] +=(-1)
       xx[ii] +=(3*n_cell-1)

#----------CB-------------
for i in xrange(0, mm):
       ii =i+4*mm
       xx[ii],yy[ii] =hc.hcindex2xy_cb(n_cell,i)
       yy[ii] +=(-n_cell-1)
       xx[ii] +=(3*n_cell-1)

#----------CB-------------
for i in xrange(0, mm):
       ii =i+5*mm
       xx[ii],yy[ii] =hc.hcindex2xy_cb(n_cell,i)
       yy[ii] +=(-n_cell-1)
       xx[ii] +=(2*n_cell-1)

#----------CB-------------
for i in xrange(0, mm):
       ii =i+6*mm
       xx[ii],yy[ii] =hc.hcindex2xy_cb(n_cell,i)
       yy[ii] +=(-n_cell-1)
       xx[ii] +=(n_cell-1)

#----------AD-------------
for i in xrange(0, mm):
       ii =i+7*mm
       xx[ii],yy[ii] =hc.hcindex2xy_ad(n_cell,i)
       yy[ii] +=(-n_cell)
       
#----------ad-------------
for i in xrange(0, mm):
       ii =i+8*mm
       xx[ii],yy[ii] =hc.hcindex2xy_ad(n_cell,i)
       yy[ii] +=(-n_cell)
       xx[ii] +=n_cell

       
plt.plot(xx, yy)
plt.title('HilbertCurve_sample2')
v = [numpy.min(xx)-2, numpy.max(xx)+2,numpy.min(yy)-1,numpy.max(yy)+1]
plt.axis(v)
plt.show()
#image = numpy.zeros((n,n))
#plt.pcolor(distance)
#plt.colorbar() 
