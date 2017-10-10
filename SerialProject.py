#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vectorizer import cluster_paragraphs
import os
import time

start_time = time.time()
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
#Luego de obtener el texto de cada documento se pasa a un vector con el cual analizaremos la similaridad

num_clusters =8
cluster_paragraphs(dataset, num_clusters,filecontent)
clusters = cluster_paragraphs(dataset, num_clusters,filecontent)

cont = 0
for group in clusters:
	print('\nGroup {0}'.format(cont))
	print '\n'.join(t for t in clusters[cont])
	cont = cont + 1
print '\n\n\n'

print("The execution time was %s seconds" % (time.time() - start_time))