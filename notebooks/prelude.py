""" IPython prelude code """

#
# Startup...
#
print("Running prelude")

#
# System imports
#
import os
import sys
import requests
import string
import random
import warnings
import argparse

from functools import *
from pathlib import Path

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
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from matplotlib import rc

#
# Import ipywidgets
#
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

#
# Try to import networkx
#
have_networkx = True
try:
    import networkx as nx
except ImportError:
    have_networkx = False

#
# Use rc to configure animation for HTML5
#
rc('animation', html='jshtml')

#
# Import tensor class
#
import importlib
import subprocess

#
# Parse the arguments
#
print("")

parser = argparse.ArgumentParser()

parser.add_argument('--style')
parser.add_argument('--animation')
parser.add_argument('--logger', default=False, action='store_true')
parser.add_argument('--verbose', default=False, action='store_true')


args = parser.parse_args()

#
# Import fibertree package (optionally installing it from github)
#
try:
    module_name = 'fibertree'
    importlib.import_module(module_name)
    print(f"The {module_name} module is already installed and available to import")
except ImportError:
    print(f"The {module_name} module is not available. Installing...")
    # Define the pip command to execute
    pip_command = ['pip', 'install', 'git+https://github.com/Fibertree-Project/fibertree', '--quiet']
    # Execute the pip command
    subprocess.call(pip_command)


from fibertree import Payload, Fiber, CoordPayload, Tensor
from fibertree import TensorImage, TensorCanvas, CycleManager
from fibertree import NotebookUtils, TensorMaker, TensorDisplay

#
# Pick up some old utility functions (their use  should be deprecated)
#
from fibertree.notebook.notebook_utils import *

#
# Instantiate the Notebook Utilities class
#
NB = NotebookUtils()

if args.logger:
    NB.showLogging()

#
# Instantiate the Tensor Display class
#
# This object holds the current styles for displaying and animating the tensors.
#
FTD = TensorDisplay(style=args.style,
                    animation=args.animation,
                    have_ipywidgets=True)

#
# Convenience functions that just call the class methods on the FTD
# object created above. 
#
displayTensor = FTD.displayTensor
displayGraph = FTD.displayGraph
createCanvas = FTD.createCanvas
displayCanvas = FTD.displayCanvas

#
# Create a runall button (but not in colab)
#
if 'COLAB_JUPYTER_IP' not in os.environ:
    NB.createRunallButton()


#
# Utility function to download data for use in the notebook environment
#
def download_github_directory(user, repo, directory):
    """ Download files from a github repo's directory """

    api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{directory}"
    response = requests.get(api_url)
    if response.status_code == 200:
        contents = response.json()
        if not os.path.exists(directory):
            os.makedirs(directory)
        for item in contents:
            download_url = item["download_url"]
            file_name = item["name"]
            response = requests.get(download_url)
            if response.status_code == 200:
                with open(os.path.join(directory, file_name), "wb") as file:
                    file.write(response.content)
                    if args.verbose:
                        print(f"Downloaded: {file_name}")
            else:
                print(f"Failed to download: {file_name}")
    else:
        print("Failed to fetch directory contents.")


def download_data(verbose=True):
    """ Download fibertree data (if not already available) """

    for data_dir in ["../../data", "../data", "./data"]:
        if os.path.exists(data_dir):
            if verbose:
                print(f"Data directory exists at: {data_dir}")
            return Path(data_dir)

    download_github_directory("Fibertree-Project",
                              "fibertree-notebooks",
                              "data")

    data_dir = "./data"
    print(f"Data directory downloaded to: {data_dir}")
    return Path(data_dir)


#
# Create datafile name (for backwards compatibility)
#
def datafileName(filename):
    """ Get fibertree data file """

    data_dir = download_data(verbose=False)

    return data_dir / filename
