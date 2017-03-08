# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:12:22 2017

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
import timeserieprocess as tsp

np.savetxt('test.txt', mm,fmt="%2.3f", delimiter=",",header='# Date Open High Low Close Volume',comments='time series data')
