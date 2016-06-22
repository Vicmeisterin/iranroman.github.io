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

        # TODO: train the algorithm
        
        self.X_train = X
        self.y_train = y
    
    def predict(self, X, k=1, L=1):

        dists = self.compute_distances(X, L=1)

        return self.predict_labels(dists, k=k)

    def compute_distances(self, X, L=1):
        
    ########
    ## TODO: generate the distance matrix by 
    ## calculating either the L1 or L2 norm,
    ## depending in what value for L the user
    ## passes. This implementation SHOULD NOT!
    ## be vectorized. Use two loops and a couple
    ## if statements to select between the L1 and L2
    ## distances. Overall, this should be very
    ## similar to what we have done in class so far.
    ########

        dists = np.zeros((X.shape[0], self.X_train.shape[0]))
        
        for i in xrange(X.shape[0]):
            for j in xrange(self.X_train.shape[0]):

                if L == 1:
                    dists[i,j] = np.sum(np.abs(self.X_train[j,:] - X[i,:]))

                if L == 2:
                    dists[i,j] = np.sqrt(np.sum((self.X_train[j,:] - X[i,:])**2))


        return dists

    def predict_labels(self, dists, k=1):

        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)
        for i in xrange(num_test):
    
            # TODO:
            # 1. sort the elements in the ith row in the dists matrix, use np.argsort
            dists_i_row_sorted=np.argsort(dists[i,:]) 
            # 2. find the labels for the top k closes training points
            k_closest_labels=self.y_train[dists_i_row_sorted[:k]]   

            # 3. count the number of times each label is repeated for the k closest training points
            # use np.bincount
            arr_w_k_incidences = np.bincount(k_closest_labels)
            # 4. find the most repeating label, or the smaller label to break ties
            # use np.argmax
            y_pred[i]=np.argmax(arr_w_k_incidences)
      
        return y_pred

#     #### UNCOMMENT from here until the end of this file
#     #### to work on the extension of this assignment
#     #### IGNORE if you have not completed steps 1, 2, and 3
#     #### described in the 'Exercise 2' document

#     def compute_distances_one_loop(self, X, L=1):

#         #implement a version of this function where you only use one for loop

#         return dists

#     def compute_distances_vectorized(self, X, L=1):

#         #implement a version of this function where you don't use loops

#         return dists

