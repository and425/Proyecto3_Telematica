#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpi4py import MPI
from vectorizer import cluster_paragraphs
import os
import time
import numpy
start_time = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

path ='./txt'
dataset =[]
filecontent = []
filecontentSplited = []
if rank == 0:
    files = [f for f in os.listdir(path) if os.path.split(f)]
    for f in files:
        if f.endswith(".txt"):
            filecontent.append(f)
    filecontentSplited = numpy.array_split(numpy.array(filecontent),size)
else:
    data = None

data = comm.bcast(filecontentSplited, root=0)
for d in data[rank]:
    j = os.path.join(path, d)
    d=open(j, 'r').read().replace('\n', '')
    if rank != 0:
        comm.send(d,dest=0)
    else:
        dataset.append(d)

if rank == 0:
    for i in range(size):
        data = comm.recv(source=MPI.ANY_SOURCE)
        dataset.append(data)

print("Rank ",rank," The execution time was %s seconds" % (time.time() - start_time))