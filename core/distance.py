import numpy as np

class Distance:
    @staticmethod
    def euclidean(a, b):
        return np.sqrt(np.sum((a - b) ** 2))