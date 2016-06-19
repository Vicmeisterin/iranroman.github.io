"""
Original by Andrej Kaparthy, Fei Fei Li, and Justin Johnson
modified by Iran Roman
"""

import numpy as np

class KNN(object):
  """ a kNN classifier with L2 and L1 distances """

  def __init__(self):
    pass

  def train(self, X, y):

    self.X_train = X
    self.y_train = y
    
  def predict(self, X, k=1, L=1):

    dists = self.compute_distances(X, L=1)

    return self.predict_labels(dists, k=k)

  def compute_distances(self, X, L=L1):

        #####################################################################
        # TODO:                                                             #
        # Compute the L2 and L1 distances between the ith test point and 	#
        # the jth training point, and store the result in dists[i, j].      #
        #####################################################################

    return dists

  def predict_labels(self, dists, k=1):

    num_test = dists.shape[0]
    y_pred = np.zeros(num_test)
    for i in xrange(num_test):
      # A list of length k storing the labels of the k nearest neighbors to
      # the ith test point.
      closest_y = []

      # TODO:
      # 1. sort the elements in the ith row in the dists matrix, use np.argsort
      
      # 2. find the labels for the top k closes training points
      
        
      # 3. count the number of times each label is repeated for the k closest training points
      # use np.bincount
      
      # 4. find the most repeating label, or the smaller label to break ties
      # use np.argmax
      
    return y_pred
