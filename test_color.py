# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:17:30 2017

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

#mm = tsp.processFile("stocksApple.txt",4,256,1)

mm = tsp.processFile("stocksFord.txt",4,256,1)


