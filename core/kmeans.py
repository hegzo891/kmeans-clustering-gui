import numpy as np
import random
from core.distance import Distance

class KMeans:
    def __init__(self, k, max_iter=100):
        self.k = k
        self.max_iter = max_iter
        self.centroids = None

    def initialize_centroids(self, data):
        indices = random.sample(range(len(data)), self.k)
        self.centroids = data[indices]

    def assign_clusters(self, data):
        clusters = []
        for point in data:
            distances = [Distance.euclidean(point, c) for c in self.centroids]
            clusters.append(np.argmin(distances))
        return np.array(clusters)

    def update_centroids(self, data, clusters):
        new_centroids = []
        for i in range(self.k):
            points = data[clusters == i]
            if len(points) > 0:
                new_centroids.append(points.mean(axis=0))
            else:
                new_centroids.append(data[random.randint(0, len(data)-1)])
        self.centroids = np.array(new_centroids)

    def fit(self, data):
        self.initialize_centroids(data)

        for _ in range(self.max_iter):
            clusters = self.assign_clusters(data)
            old_centroids = self.centroids.copy()

            self.update_centroids(data, clusters)

            if np.allclose(old_centroids, self.centroids):
                break

        return clusters