
# coding: utf-8

# In[1]:

import numpy as np

# finding support
sigma = np.array([1/3,1/2,0,0,1/6])
np.where(sigma > 0)


# In[2]:

sigma = np.array([0,0,1,0])
np.where(sigma > 0)


# In[4]:

# degenerate games
A = np.array([[1,1,0], [2,3,0]])
sigma_c = np.array([0,0,1])
(np.dot(A,sigma_c))


# In[5]:

# support enumeration algorithm
# matching pennies
import nashpy as nash
A = np.array([[1,-1], [-1,1]])
game = nash.Game(A)
list(game.support_enumeration())


# In[6]:

# larger games
A = np.array([[1,1,-1], [2,-1,0]])
B = np.array([[1/2,-1,-1/2], [-1,3,2]])
game = nash.Game(A, B)
list(game.support_enumeration())


# In[7]:

A = np.array([[1,1,0], [2,-1,0]])
B = np.array([[1/2,-1,-1/2], [-1,3,2]])
game = nash.Game(A, B)
list(game.support_enumeration())


# In[ ]:



