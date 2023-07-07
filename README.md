Fibertree Notebooks
===================

This repository contains various Jupyter notebooks that illustrate the
implemention of various sparse (and dense) computations using the
fibertree abstraction.


Run in Google Colab
===================

The notebooks in this repo can be run in Google Colab and will bootstrap
an environment using [fibertree-bootstrap](https://github.com/Fibertree-Project/fibertree-bootstrap).

To run them, go to the `notebooks` directory in the
[fibertree notebooks](https://github.com/Fibertree-Project/fibertree-notebooks) repo and pick
a notebook to open in Colab, which is very convenient using the ["Open
in Colab"](https://chrome.google.com/webstore/search/open%20in%20colab)
Chrome extension.

Some notebooks that you can run in Colab directly are:

- [startup page](https://colab.research.google.com/github/Fibertree-Project/fibertree-notebooks/blob/master/notebooks/start-here.ipynb) - a directory of notebooks
- [fibertree demo](https://colab.research.google.com/github/Fibertree-Project/fibertree-notebooks/blob/master/notebooks/basic/fibertree.ipynb) - an initial tutorial notebook


Run in a Docker container
=========================

The [fibertree-docker](https://github.com/Fibertree-Project/fibertree-docker)
repository provides a Docker container with a preinstalled copy of the
fibertree package and where one can run the fibertree notebooks
without additional local installation.


Manual local installation
=========================

See the [fibertree](https://github.com/Fibertree-Project/fibertree)
repository for instructions on installing the fibertree Python package.

Then clone this repository and run the Jupyter notebooks:

```console
cd fibertree-notebooks/notebooks
jupyter lab .
```

Browse in the various subdirectories and invoke
a notebook. A good place to start is basic/fibertree.ipynb

See FAQ below for addressing some problems.


Python virtual environment installation
=======================================

Create virtual environment and install required packages

```console
python -m venv <directory-for-venv>
source <directory-for-venv>/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install git+https://github.com/Fibertree-Project/fibertree
```

Get the fibertree notebooks

```console
git clone https://github.com/Fibertree-Project/fibertree-notebooks

cd fibertree-notebooks/notebooks
jupyter lab .
```

When done, deactivate the virtual environment

```console
deactivate
```



Development
===========

To clear out the outputs from modified notebooks, run the following:

```console
for i in `git diff --name-only`; do jupyter nbconvert --clear-output --inplace $i; done
```

FAQ
===

Q: How do I fix font-related errors when displaying graphics?

A: On Ubuntu/Debian systems you can try installing fonts-freefon-ttf with:

```console
sudo apt install fonts-freefont-ttf
```

   If you know where the fonts are on your system then you can set the
   environment variable FIBERTREE_FONT in Python code you can do this
   with something like:

```python
   import os

   os.environ['FIBERTREE_FONT'] = 'Pillow/Tests/fonts/FreeMono.ttf'
```

Q: How can I get the Jupyter widgets to work?

A1: For classic Jupyter notebooks, try the following command:

```console
jupyter nbextension enable --py widgetsnbextension
```

A2: To get widgets to work in Jupyter lab, try the following:

```console
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash
# restart bash
nvm install node
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```


