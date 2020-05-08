#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# evolutionary dynamics

#reproduction 

import sympy as sym
sym.init_printing()
x = sym.Function('x')
t, a = sym.symbols('t, a')
sym.dsolve(sym.Derivative(x(t), t) - a * x(t), x(t))

import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from scipy.integrate import odeint

t = np.linspace(0, 10, 100)  # Obtain 100 time points


def dx(x, t, a):
    """Define the derivate of x"""
    return a * x

a = 10
xs = odeint(func=dx, y0=1, t=t, args=(a,))
plt.plot(xs);

a = -10
xs = odeint(func=dx, y0=1, t=t, args=(a,))
plt.plot(xs);

# selection

def drho(rho, t, a, b):
    """Define the derivate of x"""
    return (a - b) * rho

a, b = 10, 5
rhos = odeint(func=drho, y0=1, t=t, args=(a, b))
plt.plot(rhos);

# selection with constant population size

def dxy(xy, t, a, b):
    """
    Define the derivate of x and y. 
    It takes `xy` as a vector
    """
    x, y = xy
    phi = a * x + b * y
    return x * (a - phi), y * (b - phi)

a, b = 10, 5
xys = odeint(func=dxy, y0=[.5, .5], t=t, args=(a, b))
plt.plot(xys);

a, b = 10, 5
xys = odeint(func=dxy, y0=[1, 0], t=t, args=(a, b))
plt.plot(xys);

a, b = 10, 5
xys = odeint(func=dxy, y0=[0, 1], t=t, args=(a, b))
plt.plot(xys);

a, b = 5, 5
xys = odeint(func=dxy, y0=[.5, .5], t=t, args=(a, b))
plt.plot(xys);

