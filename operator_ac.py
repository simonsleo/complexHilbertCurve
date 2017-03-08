# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:18:32 2017

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
m=2
n_cell=2**m
mm = n_cell*n_cell

n=2**(m+1)

xx = numpy.zeros(n**2, dtype=numpy.int16)
yy = numpy.zeros(n**2, dtype=numpy.int16)
for i in xrange(0, n**2):
       xx[i],yy[i] =hc.hcindex2xy_ca(n,i)
plt.plot(xx, yy)
plt.title('CA')
v = [numpy.min(xx)-2, numpy.max(xx)+2,numpy.min(yy)-1,numpy.max(yy)+1]
plt.axis(v)
plt.show()