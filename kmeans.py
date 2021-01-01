from math import pow, sqrt
import numpy as np
from random import uniform, random
import matplotlib.pyplot as plt


def distance(p1, p2):
    if len(p1) != len(p2):
        raise TypeError("points must be in the same dimensions")
    total = 0
    for x, y in zip(p1, p2):
        total += pow((x - y), 2)
    return sqrt(total)


class Cluster:
    def __init__(self, location=(), points=[]):
        self.points = points
        if not location:
            self.set_location()
        else:
            self.location = location
        self.prev_location = None

    def total_euclidean_distance(self):
        return sum([distance(point, self.location) for point in self.points])

    def distances(self):
        distances = {}
        for point in self.points:
            distances[point] = distance(self.location, point)
        return distances

    def set_location(self):
        total = []
        for point in self.points:
            for i, dim in enumerate(point):
                try:
                    total[i] += dim
                except:
                    total.append(dim)
        total = np.array(total)
        total = total / len(self.points)
        self.prev_location = self.location
        self.location = tuple(total)
        return self.location

    def converged(self):
        return self.prev_location == self.location


class Clusters:
    def __init__(self, cluster_count=2, dataset=[]):
        self.cluster_count = cluster_count
        self.dataset = dataset
        self.clusters = []
        self.locations = []

    def run(self):
        intervals = self.range()
        for _ in range(self.cluster_count):
            location = []
            for interval in intervals:
                location.append(uniform(interval[0], interval[1]))
            self.locations.append(tuple(location))

        self.clusters = [Cluster(self.locations[num], points=self.dataset) for num in range(self.cluster_count)]

        while not self.converged():
            self.reassign()

    def reassign(self):
        best = {}
        for i, cluster in enumerate(self.clusters):
            distances = cluster.distances()
            for key in distances:
                if key not in best:
                    best[key] = (i, distances[key])
                else:
                    if best[key][1] > distances[key]:
                        best[key] = (i, distances[key])

        for cluster in self.clusters:
            cluster.points = []

        for point in best:
            cluster = best[point][0]
            self.clusters[cluster].points.append(point)

        for cluster in self.clusters:
            cluster.set_location()

    def converged(self):
        for cluster in self.clusters:
            if not cluster.converged():
                return False
        return True

    def range(self):
        low = [num for num in self.dataset[0]]
        high = [num for num in self.dataset[0]]
        for point in self.dataset[1:]:
            for i, dim in enumerate(point):
                if dim > high[i]:
                    high[i] = dim
                elif dim < low[i]:
                    low[i] = dim
        return [(low, high) for low, high in zip(low, high)]
