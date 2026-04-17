import numpy as np
from core.distance import Distance

class OutlierDetector:
    def __init__(self, threshold=2.5):
        self.threshold = threshold

    def detect(self, data, clusters, centroids):
        outliers = []

        for i, point in enumerate(data):
            cluster = clusters[i]
            dist = Distance.euclidean(point, centroids[cluster])

            cluster_points = data[clusters == cluster]
            distances = [Distance.euclidean(p, centroids[cluster]) for p in cluster_points]

            mean = np.mean(distances)
            std = np.std(distances)

            if std > 0 and (dist - mean) / std > self.threshold:
                outliers.append(i)

        return outliers