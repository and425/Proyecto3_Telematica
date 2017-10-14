#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpi4py import MPI
from Pvectorizer import cluster_paragraphs
import os
import time
import numpy
start_time = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

dataset =[]
filecontent = []
path ='./txt'
files = [f for f in os.listdir(path) if os.path.split(f)]

for f in files:
    if f.endswith(".txt"):
        filecontent.append(f)

for f in filecontent:
    j = os.path.join(path, f)
    with open(j, 'r') as myfile:
        data=myfile.read().replace('\n', '')
        dataset.append(data)
    
num_clusters = 4
cluster_paragraphs(dataset, num_clusters,filecontent)
clusters = cluster_paragraphs(dataset, num_clusters,filecontent)


comm.Barrier()
cont = 0 #usado para identificar el numero de los subgrupos
aux = ""
data = None
if rank != 0:
    comm.send(clusters,dest=0,tag=11)

if rank == 0:
    data = comm.recv(source=MPI.ANY_SOURCE,tag=11)

comm.Barrier()
if rank == 0:
    for group in clusters:
        print('\nGroup {0}'.format(cont))
        print '\n'.join(t for t in clusters[cont])
        print '\n'.join(t for t in data[cont])
        print "------"
        cont = cont + 1
    print '\n\n\n'

print("Rank ",rank," The execution time was %s seconds" % (time.time() - start_time))