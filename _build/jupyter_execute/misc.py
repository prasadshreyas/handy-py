#!/usr/bin/env python
# coding: utf-8

# #  Misc Python Tricks

# Let's say if you want to initialize a list of size $n$ with zeros, you can use this trick:

# In[1]:


[0] * 5


# You can also use this to initialize a matrix of size $n \times m$ with zeros

# In[2]:


[[0] * 3] * 3


# But when try to initialize a matrix of size $n \times m$ with random numbers, you can't do this:

# In[3]:


# Initialize a random array of size 5 with values between 0 and 10
import random
a = [random.randint(0, 10)] * 5
a


# This is because the random numbers are not generated for each element of the list but rather the same random number is **copied** $n$ times. To fix this, you can use list comprehension.

# In[4]:


[random.randint(0, 10) for i in range(5)]


# Same thing applies to initializing a matrix of size $n \times m$

# In[5]:


a = [[random.randint(0, 10) for i in range(3)] for j in range(3)]
a


# Analyzing the time complexity of an algorithm and comparing it with other algorithms is a very important part of the preparing for interview process. In Python, there are a few ways to measure the time of a function. The most common way is to use the `time` module. 
# 
# To measure the time of a function, `%timeit` is a very useful tool. It will run the function multiple times and give you the average time it took to run the function. 

# In[6]:


def test():
    for i in range(100000):
        pass

get_ipython().run_line_magic('timeit', 'test()')


# List comprehension is a very useful tool for sorting a nested list. Let's say you have a list of lists and you want to sort it by the second element of each list. You can do this:

# In[7]:


a = [[10, 2, 17], [9, 3, 9],[4,1,2]]
a.sort(key=lambda x: x[1])
a


# Random
# ---

# The `random` module has a lot of useful functions. Here are a few that I've found useful.
# 
# - Randomly shuffle a list of numbers. (Useful for generating test cases)
# - Generate a random integer between $a$ and $b$.

# In[8]:


import random
a = [1, 2, 3, 4, 5]

random.shuffle(a)
a


# Datetime
# ---
# 
# The `datetime` module is very useful for working with dates and times. For example, you can use it to get the current date and time.

# In[9]:


import datetime

datetime.datetime.now()


# `datetime.datetime.now()` will return a `datetime` object with the current date and time. You can use the `strftime` method to format the date and time.

# In[10]:


datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# The datetime function most handy for when calculating the difference between two timestamps. For example, you can use it to convert a string to a datetime object and carry out operations like `timestamp2 - timestamp1` to get the difference between two timestamps.

# In[11]:


start, end = ["2016:01:01:01:01:01", "2017:01:01:23:00:00"]
start = datetime.datetime.strptime(start, "%Y:%m:%d:%H:%M:%S")
end = datetime.datetime.strptime(end, "%Y:%m:%d:%H:%M:%S")
print((end - start))


# More
# ---
# Print a 2D array in a matrix format

# In[12]:


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=' ')
    print()

