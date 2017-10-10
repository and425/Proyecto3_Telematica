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

data = comm.scatter(filecontentSplited, root=0)
#comm.Barrier()
#print "im rank" , rank, "and my data is ", data

for d in data:
    j = os.path.join(path, d)
    d=open(j, 'r').read().replace('\n', '')
    '''
    if rank != 0:
        
        #comm.send(d,dest=0)
    else:
        dataset.append(d)
    '''
#if rank != 0:
#    comm.send(None,dest=0)
newdata = comm.gather(d, root = 0)
#dataset = dataset.append(d)

if rank == 0:
    #while True:
        #data = comm.recv(source=MPI.ANY_SOURCE)
        #if data == None:
        #    print "paso algo"
        #    break
        dataset.append(newdata)
      
print("Rank ",rank," The execution time was %s seconds" % (time.time() - start_time))
#print dataset