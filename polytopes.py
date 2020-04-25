
# coding: utf-8

# In[2]:

# polytopes
# as a convex hull
get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial

V = [
    np.array([0,0]),
    np.array([1/2,0]),
    np.array([1/2,1/4]),
    np.array([0,1/3])   
]

P= scipy.spatial.ConvexHull(V)
scipy.spatial.convex_hull_plot_2d(P);


# In[4]:

# best reponses polytope
import sympy as sym
x_1 = sym.symbols('x_1')
sym.solveset(1/3 - x_1 / 3 - 1 + 3 * x_1, x_1)


# In[5]:

V = [
    np.array([0,0]),
    np.array([1/3,0]),
    np.array([1/4,1/4]),
    np.array([0,1/3])   
]
P= scipy.spatial.ConvexHull(V)
scipy.spatial.convex_hull_plot_2d(P);


# In[6]:

# vertex enumeration algorithm
import nashpy as nash
A = np.array([[1,-1], [-1,1]])
matching_pennies = nash.Game(A)
list(matching_pennies.vertex_enumeration())


# In[ ]:



