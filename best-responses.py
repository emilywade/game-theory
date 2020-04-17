
# coding: utf-8

# In[5]:

import sympy as sym
import numpy as np
sym.init_printing()

x, y = sym.symbols('x, y')
A = sym.Matrix([[1,-1], [-1,1]])
B = -A
sigma_r = sym.Matrix([[x,1-x]])
sigma_c = sym.Matrix([y,1-y])
A * sigma_c, sigma_r * B


# In[8]:

import matplotlib
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
matplotlib.rc("savefig", dpi=100) # increases quality of images

ys = [0,1]
row_us = [[(A * sigma_c)[i].subs({y: val}) for val in ys] for i in range(2)]
plt.plot(ys, row_us[0], label="$(A\sigma_c^T)_1$")
plt.plot(ys, row_us[1], label="$(A\sigma_c^T)_2$")
plt.xlabel("$\sigma_c=(y, 1-y)$")
plt.title("Utility to row player")
plt.legend();


# In[10]:

xs = [0,1]
row_us = [[(sigma_r * B)[j].subs({x: val}) for val in xs] for j in range(2)]
plt.plot(xs, row_us[0], label="$(\sigma_rB)_1$")
plt.plot(xs, row_us[1], label="$(\sigma_rB)_2$")
plt.xlabel("$\sigma_r=(x, 1-x)$")
plt.title("Utility to column player")
plt.legend();


# In[ ]:



