#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Evolutionary Game Theory
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.integrate import odeint

t = np.linspace(0, 10, 100) # obtain 100 time points

def dx(x, t, A):
    """
    Define the derivative of x
    """
    f = np.dot(A, x)
    phi = np.dot(f, x)
    return x * (f - phi)


# In[1]:


# a>c
A = np.array([[4, 3], [2, 1]])
epsilon = 10 ** -1
xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
plt.plot(xs);

# a=c and b>d 
A = np.array([[4, 3], [4, 1]])
epsilon = 10 ** -1
xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
plt.plot(xs);

# a=c and b<d
A = np.array([[4, 3], [4, 5]])
epsilon = 10 ** -1
xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
plt.plot(xs);

# a<c
A = np.array([[1, 3], [4, 1]])
epsilon = 10 ** -1
xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
plt.plot(xs);


# In[3]:


import nashpy as nash
game = nash.Game(A,A.transpose())
list(game.support_enumeration())

import sympy as sym
sym.init_printing()
A = sym.Matrix(A)
y_1, y_2 = sym.symbols("y_1, y_2")
y = sym.Matrix([y_1, y_2])
A, y


# In[ ]:




