
# coding: utf-8

# In[1]:

# BATTLE OF THE SEXES

import nashpy as nash
A = [[3,1], [0,2]]
B = [[2,1], [0,3]]

battle_of_the_sexes = nash.Game(A,B)
battle_of_the_sexes


# In[2]:

# PRISONER'S DILEMMA

A = [[3,0], [5,1]]
B = [[3,5], [0,1]]

prisoners_dilemma = nash.Game(A,B)
prisoners_dilemma


# In[3]:

# HAWK DOVE GAME

A = [[0,3], [1,2]]
B = [[0,1], [3,2]]

hawk_dove = nash.Game(A,B)
hawk_dove


# In[4]:

# PIGS

A = [[4,2], [6,0]]
B = [[2,3], [-1,0]]

pigs = nash.Game(A,B)
pigs


# In[5]:

# MATCHING PENNIES

A = [[1,-1], [-1,1]]
B = [[-1,1], [1,-1]]

matching_pennies = nash.Game(A,B)
matching_pennies


# In[6]:

# ZERO SUM GAME

A = [[1,-1],[-1,1]]

matching_pennies = nash.Game(A)
matching_pennies


# In[ ]:



