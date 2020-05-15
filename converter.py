#!/usr/bin/env python3

from cv2 import imread

from rm4sccdec import rm4scc, processing, statistics

class converter:
    """
    Provides an API adaptor to the underlying OpenCV and RM4SCC decoder classess. 
    """

    def __init__(self):
        pass

    def decode(self, path):
        """
        Decodes the RM4SCC/CBC from the specified image. 

        :param path: path to the image to decode.
        :returns: string with image data
        """

        # Process the raw image data
        img = imread(path)
        processed = processing.prepareImage(img)
        contours = processing.findContours(processed)

        # Do some math to identify the peaks 
        features = statistics.getFeatures(contours)
        initial_centroids = statistics.computeClusteringInitialPoints(features)

        symbols, centroids = statistics.classifySymbols(features, initial_centroids)

        # Decode the encoded data
        codeword = rm4scc.RM4SCC.decodeSymbols(list(symbols))
        return codeword