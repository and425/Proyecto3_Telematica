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

'''
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

#Parte para ver todos los archivos tipo txt y guardarlos en una lista

dataset =[]
filecontent = []
path ='./txt'
files = [f for f in os.listdir(path) if os.path.split(f)]

for f in files:
    if f.endswith(".txt"):
        filecontent.append(f)
#Vamos a ver como pasar el contenido del txt para poder analizarlo

for f in filecontent:
    j = os.path.join(path, f)
    with open(j, 'r') as myfile:
        data=myfile.read().replace('\n', '')
        dataset.append(data)
    
num_clusters = 4
cluster_paragraphs(dataset, num_clusters,filecontent)
clusters = cluster_paragraphs(dataset, num_clusters,filecontent)

#newdata = comm.gather(data, root = 0)
cont = 0 #usado para identificar el numero de los subgrupos

for group in clusters:
    print('\nGroup {0}'.format(cont))
    print '\n'.join(t for t in clusters[cont])
    cont = cont + 1
print '\n\n\n'


print("Rank ",rank," The execution time was %s seconds" % (time.time() - start_time))
#print dataset