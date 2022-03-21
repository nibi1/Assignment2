#!/usr/bin/env python
# coding: utf-8

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# 
# 
# 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# In[6]:


l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i][1] < l1[j][1]:
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp
print(l1)


# In[7]:


l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l1.sort(key = lambda j:j[1])
print(l1)

