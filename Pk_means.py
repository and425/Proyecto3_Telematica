#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpi4py import MPI
from similarity import similarity
import time
import random

class KMeans(object):
    """K-Means clustering. Uses cosine similarity as the distance function."""

    def __init__(self, k, vectors):
        assert len(vectors) >= k
        self.centers = random.sample(vectors, k)
        self.clusters = [[] for c in self.centers]
        self.vectors = vectors

    def update_clusters(self):
        """Determine which cluster center each `self.vector` is closest to."""
        def closest_center_index(vector):
            """Get the index of the closest cluster center to `self.vector`."""
            similarity_to_vector = lambda center: similarity(center,vector)
            center = max(self.centers, key=similarity_to_vector)
            return self.centers.index(center)

        self.clusters = [[] for c in self.centers]
        vectorsSplited = numpy.array_split(numpy.array(vectors),size)
        data = comm.scatter(vectorsSplited, root=0)
        for vector in data:
             index = closest_center_index(vector)
             self.clusters[index].append(vector)
        newdata = comm.gather(self.clusters, root = 0)
        if rank == 0:
            self.clusters.append(newdata)
            
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
