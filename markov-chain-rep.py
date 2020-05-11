#!/usr/bin/env python
# coding: utf-8

# In[1]:


#RETURNS MARKOV REP OF GAME BETWEEN 2 REACTIVE PLAYERS 

import numpy as np
import itertools

def make_matrix(p, q):
    """
    Code to obtain Markov chain representation of match between two reactive players.
    """
    M = [[ele[0] * ele[1] for ele in itertools.product([player, 1 - player], 
                                                       [opponent, 1 - opponent])]
         for opponent in q for player in p]
    return np.array(M)

def theoretic_steady_state(p, q):
    r_1 = p[0] - p[1]
    r_2 = q[0] - q[1]
    s_1 = (q[1] * r_1 + p[1]) / (1 - r_1 * r_2)
    s_2 = (p[1] * r_2 + q[1]) / (1 - r_1 * r_2)
    return np.array([s_1 * s_2, s_1 * (1 - s_2), (1 - s_1) * s_2, (1 - s_1) * (1 - s_2)])

# CHANGE RSTP VALUES IF NOT USUAL PD UTILITIES
def theoretic_utility(p, q, rstp=np.array([3, 0, 5, 1])):
    pi = theoretic_steady_state(p, q)
    return np.dot(pi, rstp)


# In[5]:


# ONLY THING TO CHANGE HERE 

import sympy as sym
for p, q in [([sym.S(1) / 2, sym.S(1) / 2], [sym.S(1) / 2, sym.S(1) / 2]),
             ([sym.S(1) / 4, sym.S(1) / 2], [sym.S(1) / 2, sym.S(1) / 4]),
             ([sym.S(1) / 3, sym.S(1) / 3], [sym.S(2) / 3, sym.S(1) / 4]),
             ([sym.S(1), sym.S(1) / 2], [sym.S(1), sym.S(0)])
            ]:
    print("=====")
    print(p, q)
    print("gives:")
    print(make_matrix(p, q))
    print("With utility:", theoretic_utility(p, q), theoretic_utility(q, p))


# In[ ]:




