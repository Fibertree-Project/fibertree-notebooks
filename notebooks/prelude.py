""" IPython prelude code """
#
# Argument parsing imports
# Note: to guide animation display since people often do "Run All Cells"
#
import argparse

#
# System imports
#
import os
import string
import random
import warnings
from functools import *

#
# Import display classes/utilities
#
from IPython.display import display
from IPython.display import Image
from IPython.display import HTML
from IPython.display import Javascript

from tqdm.notebook import tqdm, trange

#
# Math imports
#
import math

try:
    import numpy as np
except ImportError:
    print("Library numpy not available")

try:
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import imshow
    from matplotlib import rc
except ImportError:
    print("Library matplotlib not available")

#
# Try to import networkx
#
have_networkx = True
try:
    import networkx as nx
except ImportError:
    have_networkx = False

#
# Try to import ipywidgets
#
have_ipywidgets = True
try:
    import ipywidgets as widgets
    from ipywidgets import interact, interactive, fixed, interact_manual
except ImportError:
    have_ipywidgets = False

#
# Use rc to configure animation for HTML5
#
rc('animation', html='html5')

#
# Import tensor class
#
from fibertree import Payload, Fiber, CoordPayload, Tensor
from fibertree import TensorImage, TensorCanvas, CycleManager
from fibertree import NotebookUtils, TensorMaker, TensorDisplay

#
# Pick up some old utility functions (their use  should be deprecated)
#
from fibertree.notebook.notebook_utils import *


#
# Convenience functions that just call the class methods on the FTD
# object created below. That object holds the current styles for
# displaying and animating the tensors.
#
def displayTensor(tensor, highlights=[], **kwargs):
    """ displayTensor(<tensor|fiber>, hightlights=[ <point>...] ) """

    FTD.displayTensor(tensor, highlights=highlights, **kwargs)


def displayGraph(am_s):
    """ displayGraph(am_s) """

    FTD.displayGraph(am_s)


def createCanvas(*tensors, **kwargs):
    """ createCanvas """

    return FTD.createCanvas(*tensors, **kwargs)


def displayCanvas(*args, **kwargs):
    """ displayCanvas """

    FTD.displayCanvas(*args, **kwargs)

#
# Parse the arguments (deprecated)
#
parser = argparse.ArgumentParser()

parser.add_argument('--style')
parser.add_argument('--animation')
parser.add_argument('--logger', default=False, action='store_true')

args = parser.parse_args()

#
# Instantiate the Notebook Utilities class
#
NB = NotebookUtils()

if args.logger:
    NB.showLogging()

#
# Instantiate the Tensor Display class
#
FTD = TensorDisplay(style=args.style,
                    animation=args.animation,
                    have_ipywidgets=have_ipywidgets)

#
# Create a runall button
#
NB.createRunallButton()
