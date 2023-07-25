# The hierarchical fiber abstraction - aka fibertrees

## Introduction

The **fibertree** abstraction is a representation-agnostic way of
thinking about sparse and dense tensors and the operators that
manipulate those tensors. By **representation agnostic** we mean a
generic representation of a tensor that is independent of the
specifics of a particular in-memory format, such as CSR or CSF. Thus
although the costs of operations will be a function of the specific
representation, one can think of the operations on them
generically. Thus, using this representation one can explore the
algorithmic processing and operations uses by various accelerator
architectures. More background on this abstraction for representing
tensors can be found sections 8.2 and 8.3 of the book [Efficient
Processing of Deep Neural
Networks](https://doi.org/10.2200/S01004ED1V01Y202004CAC050).

The notebooks in these directories provide an introduction and
examples of use of Python implementation of operators and algorithms
on tensors (and other objects) in the fibertree abstraction. A good
starting point that includes an introduction to the basic operators
and graphical representations of tensors and sequences of operations
can be found in [fibertree basics](./basic/01-01.overview.ipynb)

## Contents

Following is a listing of directories containing various types
notebooks (in various levels of maturity) illustrating the
capabilities of representing various computations and dataflows using
fibertree-based computations. For each directory there is an `index`
in a notebook and a `README` in Markdown. Their contents are
identical, but one or the other link will work better depending on the
environment.

- **basic/** - Some basic examples of the use of the fibertree abstraction
[\[index\]](./basic/00-01.index.ipynb)
[\[README\]](./basic/README.md)

- **dense-dnn/** - Dense convolution
[\[index\]](./dense-dnn/00-01.index.ipynb)
[\[README\]](./dense-dnn/README.md)

- **sparse-dnn/** -  Sparse DNN computations
[\[index\]](./sparse-dnn/00-01.index.ipynb)
[\[README\]](./sparse-dnn/README.md)

- **dense-gemm/** -  Dense Matrix multiply (MM ) computations
[\[index\]](./dense-gemm/00-01.index.ipynb)
[\[README\]](./dense-gemm/README.md)

- **sparse-gemm/** -  Sparse spMspM computations
[\[index\]](./sparse-gemm/00-01.index.ipynb)
[\[README\]](./sparse-gemm/README.md)

- **tiling/** -  Tiling examples
[\[index\]](./tiling/00-01.index.ipynb)
[\[README\]](./tiling/README.md)

- **complex/** -  More complex forms
[\[index\]](./complex/00-01.index.ipynb)
[\[README\]](./complex/README.md)

- **graphs/** -  Graph algorityms
[\[index\]](./graphs/00-01.index.ipynb)
[\[README\]](./graphs/README.md)

- **dense-linalg/** -  Dense linear algebra
[\[index\]](./dense-linalg/00-01.index.ipynb)
[\[README\]](./dense-linalg/README.md)

- **codec/** -  Codec
[\[index\]](./codec/00-01.index.ipynb)
[\[README\]](./codec/README.md)


