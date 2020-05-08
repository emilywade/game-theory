#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Moran Processes

import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def neutral_moran(N, i=1, seed=0):
    """
    Return the population counts for the Moran process with neutral drift.
    """

    population = [0 for _ in range(i)] + [1 for _ in range(N - i)]
    counts = [(population.count(0), population.count(1))]
    np.random.seed(seed)
    while len(set(population)) == 2:
        reproduce_index = np.random.randint(N)
        eliminate_index = np.random.randint(N)
        population[eliminate_index] = population[reproduce_index]
        counts.append((population.count(0), population.count(1)))
    return counts
    
N = 6
plt.plot(neutral_moran(N=N, i=3, seed=6));


# In[2]:


def neutral_fixation(N, i=None, repetitions=10):
    """
    Repeat the neutral Moran process and calculate the fixation probability
    """
    fixation_count = 0
    for seed in range(repetitions):
        final_counts = neutral_moran(N=N, i=i, seed=seed)
        if final_counts[-1][0] > 0:
            fixation_count += 1 

    return  fixation_count / repetitions 

probabilities = [neutral_fixation(N, i=i, repetitions=500) for i in range(1, N)]
plt.scatter(range(1, N), probabilities)
plt.xlabel("$i$")
plt.ylabel("$x_i$");

N = 6
p = np.zeros((N + 1, N + 1))
p[0, 0] = 1
p[N, N] = 1
for i in range(1, N):
    for j in [i - 1, i + 1]:
        p[i, j] = i * (N - i) / (N ** 2)
    p[i, i] = 1 - sum(p[i, :])
p.round(2)

probabilities = [neutral_fixation(N, i=i, repetitions=500) for i in range(1, N)]
plt.scatter(range(1, N), probabilities, label="Simulated")
plt.plot(range(1, N), [i / N for i in range(1, N)], label="Theoretic: $i/N$", linestyle="dashed")
plt.xlabel("$i$")
plt.ylabel("$x_i$")
plt.legend();


# In[3]:


def theoretic_fixation(N, game, i=1):
    """
    Calculate x_i as given by the above formula
    """
    f_ones = np.array([(game[0, 0] * (i - 1) + game[0, 1] * (N - i)) / (N - 1) for i in range(1, N)])
    f_twos = np.array([(game[1, 0] * i + game[1, 1] * (N - i - 1)) / (N - 1) for i in range(1, N)])
    gammas = f_twos / f_ones
    return (1 + np.sum(np.cumprod(gammas[:i-1]))) / (1 + np.sum(np.cumprod(gammas)))

A = np.array([[4, 1], 
              [1, 4]])
theoretic_fixation(N=4, i=1, game=A)


# In[4]:


def moran(N, game, i=1, seed=0):
    """
    Return the population counts for 
    the Moran process on a 2 by 2 game
    """
    population = [0 for _ in range(i)] + [1 for _ in range(N - i)]
    counts = [(population.count(0), population.count(1))]
    
    np.random.seed(seed)
    
    while len(set(population)) == 2:
        
        scores = []
        
        for i, player in enumerate(population):
            total = 0
            for j, opponent in enumerate(population):
                if i != j:
                    total += game[player, opponent]
            scores.append(total)

        total_score = sum(scores)
        probabilities = [score / total_score for score in scores]
        reproduce_index = np.random.choice(range(N), p=probabilities)
        
        eliminate_index = np.random.randint(N)
        population[eliminate_index] = population[reproduce_index]
        
        counts.append((population.count(0), population.count(1)))
    return counts


def fixation(N, game, i=None, repetitions=10):
    """
    Repeat the Moran process and calculate the fixation probability
    """
    fixation_count = 0
    for seed in range(repetitions):
        final_counts = moran(N=N, i=i, game=game, seed=seed)
        if final_counts[-1][0] > 0:
            fixation_count += 1
    return  fixation_count / repetitions

N = 8
plt.plot(moran(N=N, i=1, seed=44, game=A));


# In[ ]:




