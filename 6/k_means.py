from copy import deepcopy
from dataclasses import dataclass
from functools import partial
from random import uniform
from statistics import mean, pstdev
from data_point import DataPoint

def z_scores(original):
    average = mean(original)
    sd = pstdev(original)

    if sd == 0: # Return all zeroes if there is no variation
        return[0] * len(original)

    return [(x - average) / sd for x in original]

class K_Means:
    @dataclass
    class Cluster:
        points: list
        centroid: DataPoint

    def __init__(self, k, points):
        if k < 1:
            raise ValueError('k must be >= 1')

        self._points = points
        self._z_score_normalize()
        # Initialize empty clusters with random centroids
        self._clusters = []

        for _ in range(k):
            random_point = self._random_point()
            cluster = K_Means.Cluster([], random_point)
            self._clusters.append(cluster)

    @property
    def _centroids(self):
        return [x.centroid for x in self._clusters]

    def _dimension_slice(self, dimension):
        return [x.dimensions[dimension] for x in self._points]

    def _z_score_normalize(self):
        z_scored = [[] for _ in range(len(self._points))]

        for dimension in range(self._points[0].num_dimensions):
            dimension_slice = self._dimension_slice(dimension)

            for i, z_score in enumerate(z_scores(dimension_slice)):
                z_scored[i].append(z_score)

        for i in range(len(self._points)):
            self._points[i].dimensions = tuple(z_scored[i])

    def _random_point(self):
        random_dimensions = []

        for dimension in range(self._points[0].num_dimensions):
            values = self._dimension_slice(dimension)
            random_value = uniform(min(values), max(values))
            random_dimensions.append(random_value)

        return DataPoint(random_dimensions)

    def _assign_clusters(self):
        for point in self._points:
            closest = min(self._centroids, key=partial(DataPoint.distance, point))
            i = self._centroids.index(closest)
            cluster = self._clusters[i]
            cluster.points.append(point)

    def _generate_centroids(self):
        for cluster in self._clusters:
            if len(cluster.points) == 0: # Keep the same centroid if no points
                continue

            means = []

            for dimension in range(cluster.points[0].num_dimensions):
                dimension_slice = [p.dimensions[dimension] for p in cluster.points]
                means.append(mean(dimension_slice))

            cluster.centroid = DataPoint(means)

    def run(self, max_iterations=100):
        for iteration in range(max_iterations):
            for cluster in self._clusters:
                cluster.points.clear()

            self._assign_clusters() # Find cluster each point is closest to
            old_centroids = deepcopy(self._centroids) # Record old centroids
            self._generate_centroids() # Find new centroids

            if old_centroids == self._centroids: # Have centroids moved?
                print(f'Converged after {iteration} iterations')
                return self._clusters

        return self._clusters

if __name__ == '__main__':
    point_0 = DataPoint([2.0, 1.0, 1.0])
    point_1 = DataPoint([2.0, 2.0, 5.0])
    point_2 = DataPoint([3.0, 1.5, 2.5])
    k_means_test = K_Means(2, [point_0, point_1, point_2])
    test_clusters = k_means_test.run()

    for i, cluster in enumerate(test_clusters):
        print(f'Cluster {i}: {cluster.points}')
