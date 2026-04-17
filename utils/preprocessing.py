import numpy as np

class Preprocessor:
    @staticmethod
    def normalize(data):
        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0)
        std[std == 0] = 1
        return (data - mean) / std