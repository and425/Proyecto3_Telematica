#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

#Parte para ver todos los archivos tipo txt y guardarlos en una lista
dataset =[]
filecontent = []
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if f.endswith(".txt"):
		filecontent.append(f)
for x in filecontent:
	print x
#Vamos a ver como pasar el contenido del txt para poder analizarlo

for f in filecontent:
	with open(f, 'r') as myfile:
		data=myfile.read().replace('\n', '')
		dataset.append(data)
#Luego de obtener el texto de cada documento se pasa a un vector con el cual analizaremos la similaridad

vec = TfidfVectorizer()
parameters = vec.fit_transform(dataset)

result = cosine_similarity(parameters)
#Se imprimne el resultado
print result