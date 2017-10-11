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
        print "im rank", rank, "with vector size", len(vectors)
        assert len(vectors) >= k
        self.centers = random.sample(vectors, k)
        self.clusters = [[] for c in self.centers]
        self.vectors = vectors
        comm.Barrier()

    def update_clusters(self):
        """Determine which cluster center each `self.vector` is closest to."""
        def closest_center_index(vector):
            """Get the index of the closest cluster center to `self.vector`."""
            similarity_to_vector = lambda center: similarity(center,vector)
            center = max(self.centers, key=similarity_to_vector)
            return self.centers.index(center)

        self.clusters = [[] for c in self.centers]    

        pos = rank
        while pos < len(self.vectors):
            if self.vectors[pos] != None:
                index = closest_center_index(self.vectors[pos])
                self.clusters[index].append(self.vectors[pos])
                pos += size
                #self.vectors[pos] = None
        comm.Barrier()
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



def average(sequence):
    return sum(sequence) / len(sequence)
