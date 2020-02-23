"""  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
template for generating data to fool learners (c) 2016 Tucker Balch  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
Atlanta, Georgia 30332  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
All Rights Reserved  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
Template code for CS 4646/7646  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
works, including solutions to the projects assigned in this course. Students  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
and other users of this template code are advised not to share it with others  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
or to make it available on publicly viewable websites including repositories  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
such as github and gitlab.  This copyright statement should not be removed  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
or edited.  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
We do grant permission to share solutions privately with non-students such  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
as potential employers. However, sharing with other current or future  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
GT honor code violation.  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
-----do not edit anything above this line---  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
Student Name: Tucker Balch (replace with your name)  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
GT User ID: tb34 (replace with your User ID)  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
GT ID: 900897987 (replace with your GT ID)  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
"""  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
import numpy as np  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
import math  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
# this function should return a dataset (X and Y) that will work  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
# better for linear regression than decision trees  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
def best4LinReg(seed=1489683273):
    np.random.seed(seed)
    num_rows = np.random.randint(10, 1000)
    num_feature = np.random.randint(2, 10)

    X = np.random.random((num_rows, num_feature))
    Y = np.random.random(size = (num_rows,))
    C = np.random.random((num_feature, ))
    bias = np.random.random((num_rows,))

    Y = np.matmul(X, C) + bias
    return X, Y
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
def best4DT(seed=1489683273):  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
    np.random.seed(seed)
    num_rows = np.random.randint(10, 1000)
    num_feature = np.random.randint(2, 10)

    X = np.random.random((num_rows, num_feature))
    Y = np.random.random(size = (num_rows,))


    picked_index = np.random.randint(0, num_feature)
    Y[X[:, picked_index] < 0.5] = 1
    Y[X[:, picked_index] > 0.5] = 0

    return X, Y  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
def author():  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
    return 'kwang441' #Change this to your user ID
  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
if __name__=="__main__":  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
    print("they call me Tim.")  		  	   		     			  		 			     			  	  		 	  	 		 			  		  			
