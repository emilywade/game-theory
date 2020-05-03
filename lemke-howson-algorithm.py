
# coding: utf-8

# In[2]:

# The Lemke Howson Algorithm

import nashpy as nash
import numpy as np

A = np.array([[1,-1],[-1,1]])
matching_pennies = nash.Game(A)
matching_pennies.lemke_howson(initial_dropped_label=0)


# In[3]:

# iterating over all possible starting labels 
for eq in matching_pennies.lemke_howson_enumeration():
    print(eq)


# In[ ]:



