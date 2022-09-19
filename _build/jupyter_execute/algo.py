#!/usr/bin/env python
# coding: utf-8

# # Algorithms

# Table of Contents
# ---
# 
# 1. [Graphs](#graphs)
# 2. [Dynamic Programming](#dynamic-programming)
# 3. [Greedy Algorithms](#greedy-algorithms)
# 4. [Backtracking](#backtracking)
# 5. [Miscellaneous](#miscellaneous)

# ## Graphs
# 

# Graphs are mainly represented as 
# 1. Adjacency list
# 2. Adjacency matrix
# 3. Edge list

# Adjacency list is the most common representation of a graph. It is a list of lists where each list represents a vertex and the elements of the list are the vertices that are adjacent to the vertex.

# In[1]:


matrix = [[0, 1,1], [1, 0,1], [1, 1,0]]


# > If the graph is undirected, then the adjacency list will be symmetric.
# 
# 
# Let's check if the above matrix is symmetric - (Without NumPy)

# In[2]:


def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
print(is_symmetric(matrix))


# Check if a matrix is symmetric - With NumPy

# In[3]:


import numpy as np

def is_symmetric(matrix):
    return np.allclose(matrix, np.transpose(matrix))
print(is_symmetric(matrix))


# ### Depth First Search (DFS)

# In[4]:


def dfs(adj)

