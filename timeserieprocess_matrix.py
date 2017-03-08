# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:53:33 2017

@author: sliu
"""

import matplotlib.backends.backend_pdf as pltBack
import matplotlib.lines as lines
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy
from optparse import OptionParser
import os
import sys

def processFile(filename, options_level,options_max,options_normalize,cc,rr):
    """
    read in the input and return the corresponding matrix
    input is two column, whitespace separated data. col1 is
    a position along the scale and col2 is a value.
    ------------------------------------------------------
    read time-series file as input data @LSQ
    """

    #x<<y, This is the same as multiplying x by 2**y.
    n = 1 << options_level
    m = numpy.zeros((n, n))
    x = []
    y = []
    f = open(filename, 'r')
    for lineno, line in enumerate(f, 1):
        if line.startswith('#'):
            continue
        line = line.strip()
        vals = line.split()
        if len(vals) < 2:
            continue
        if options_max < float(vals[0]):
            options_max = float(vals[0])
        x.append(float(vals[0]))
        y.append(float(vals[1]))
    x = numpy.array(x)
    y = numpy.array(y)
    if options_normalize:
        y -= numpy.average(y)
        y /= numpy.std(y)
 #--------------time series --------------------       
        plt.subplot(221)
        plt.plot(x,y)
#    cc=numpy.zeros(len(x))   
#    rr=numpy.zeros(len(x))
#-------------------------
    for i in xrange(0, len(x)):
        #c, r = hc.hcindex2xy_ac(n, int(round((n**2 - 1) * x[i] / options_max))) #find the
        c = cc[i]
        r = rr[i]        
        #cooresponding element matrix[][] of xi,yi. It's better to further treat
        # x  with average,make the intervals of x equal @LSQ
        m[r][c] += y[i]
    
    plt.subplot(223)
    plt.plot(cc,rr)
    v = [numpy.min(cc)-2, numpy.max(cc)+2,numpy.min(rr)-1,numpy.max(rr)+1]
    plt.axis(v)
    plt.subplot(222)
    plt.pcolor(m)   
    return m