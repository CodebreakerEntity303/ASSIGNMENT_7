#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Q2
encrypt = "I want to become a Data Scientist"

dict = {"a": "z", "b": "y","c": "x"}

num = encrypt[::1]

for i in dict:
    num = num.replace(i, dict[i])
print(f"{num}aca")

