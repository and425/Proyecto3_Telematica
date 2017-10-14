#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpi4py import MPI
from similarity import similarity
import time
import random
import numpy
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

class KMeans(object):
    """K-Means clustering. Uses cosine similarity as the distance function."""

    def __init__(self, k, vectors):
        assert len(vectors) >= k
        self.centers = random.sample(vectors, k)
        self.clusters = [[] for c in self.centers]
        self.vectors = vectors
        #comm.Barrier()

    def update_clusters(self):
        """Determine which cluster center each `self.vector` is closest to."""
        def closest_center_index(vector):
            """Get the index of the closest cluster center to `self.vector`."""
            similarity_to_vector = lambda center: similarity(center,vector)
            center = max(self.centers, key=similarity_to_vector)
            return self.centers.index(center)

        self.clusters = [[] for c in self.centers]

        if rank == 0:
            info = self.clusters
        else:
            info = None
        info = comm.bcast(info,root=0)
        pos = rank
        while pos < len(self.vectors):
            vector = (self.vectors)[pos]
            index = closest_center_index(vector)
            if vector != None:
                info[index].append(vector)
            pos += size
        comm.Barrier()
        self.clusters = info
        '''
        for vector in self.vectors:

            if vector != None
                index = closest_center_index(vector)
                self.clusters[index].append(vector)
                vector = None
        '''
    def update_centers(self):
        """Move `self.centers` to the centers of `self.clusters`.

        Return True if centers moved, else False.

        """
        '''
        if rank == 0:
            new_centers = []
            pos = rank
            while pos < len(self.clusters):
                cluster = self.clusters[pos]
                center = [average(ci) for ci in zip(*cluster)]
                new_centers.append(center)
                pos += size
        else:
            new_centers = []
        comm.Barrier()
        data = comm.bcast(self.clusters, root=0)
        temp_centers = []

        if rank != 0:
            pos = rank
            while pos < len(data):
                cluster = data[pos]
                center = [average(ci) for ci in zip(*cluster)]
                temp_centers.append(center)
                pos += size
        for x in temp_centers:
            comm.send(x,dest=0,tag=rank)
        if rank == 0:
            point = comm.recv(source = MPI.ANY_SOURCE, tag = MPI.ANY_TAG)
        comm.Barrier()
        '''
        new_centers = []
        for cluster in self.clusters:
            center = [average(ci) for ci in zip(*cluster)]
            new_centers.append(center)

        if new_centers == self.centers:
            return False

        self.centers = new_centers
        return True
        
    def main_loop(self):
        """Perform k-means clustering."""
        self.update_clusters()
        while self.update_centers():
            self.update_clusters()
        comm.Barrier()



def average(sequence):
    return sum(sequence) / len(sequence)
