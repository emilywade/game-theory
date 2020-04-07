
# coding: utf-8

# In[2]:

# using numpy to verify if a strategy is weakly/strictly dominated

import numpy as np
A = np.array([[3,0], [3,1]])
B = np.array([[3,3], [0,1]])

# verify that first row is weakly dominated by second row
all(A[0,:] <= A[1,:]) and any(A[0,:] < A[1,:])


# In[3]:

# verify that first column is weakly dominated by second column
all(B[:,0] <= B[:,1]) and any(B[:,0] < B[:,1])


# In[ ]:



