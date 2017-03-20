# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:53:33 2017

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

def processFile(filename,n,options_max,options_normalize,cc,rr,figure_name):
    """
    read in the input and return the corresponding matrix
    input is two column, whitespace separated data. col1 is
    a position along the scale and col2 is a value.
    ------------------------------------------------------
    read time-series file as input data @LSQ
    """

    #x<<y, This is the same as multiplying x by 2**y.
    #n = 1 << options_level
    m = numpy.zeros((n, n)) #n is the subsquare number on one axial
    x = []
    y = []
    min_cc=numpy.min(cc)
    min_rr=numpy.min(rr)
    min_color = -1.5 # 10 plus random max
    max_color = 1.5
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
#    cc=numpy.zeros(len(x))
#    rr=numpy.zeros(len(x))
#-------------------------
    for i in xrange(0, len(x)):
        #c, r = hc.hcindex2xy_ac(n, int(round((n**2 - 1) * x[i] / options_max))) #find the
        c = cc[i]-min_cc # avoid the index becoming negative int
        r = rr[i]-min_rr
        m[r][c] += y[i]

#------------------------images ---------------------------
    fig = plt.figure()
    fig.set_size_inches(1, 1)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.pcolor(m,cmap='seismic', vmin=min_color, vmax=max_color)
    plt.savefig(figure_name, dpi = 32)

    return m
