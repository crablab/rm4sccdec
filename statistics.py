import numpy as np
from scipy.cluster.vq import kmeans2

import processing
from rm4scc import RM4SCC


def getFeatures(contours):
    """Extract the relevant features from the list of contours given and return them, along with the initial
    centroids to use when clustering
    """
    features = map(processing.getAreaAndCentroid, contours)
    # Use x-position to sort, and then get rid of it
    features.sort(key=lambda t: t[1])
    features = [(area, y) for (area, x, y) in features]
    features = np.array(features)

    # To ease decoding, we define the initial centroid in the same order the symbols are defined in RM4SCC
    initial_centroids = np.array([
        [features[:,0].min(), features[:,1].mean()],  # 'S'
        [features[:,0].mean(), features[:,1].max()],  # 'D'
        [features[:,0].mean(), features[:,1].min()],  # 'U'
        [features[:,0].max(), features[:,1].mean()],  # 'L'
    ])

    return features, initial_centroids


def classifySymbols(features, initial_centroids):
    """Run the k-means algorithm against the features using initial_centroids as the starting points for clustering"""
    _, labels = kmeans2(features, initial_centroids)
    symbols = map(lambda i: RM4SCC.symbols[i], labels)

    return symbols