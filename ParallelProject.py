#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpi4py import MPI
from vectorizer import cluster_paragraphs
import os
import time

start_time = time.time()



print("The execution time was %s seconds" % (time.time() - start_time))