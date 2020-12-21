#!/usr/bin/env python
# coding: utf-8

# ### Plotting of Step Intensities
# 
# Simple plotting of step intensities after extracting relevant information from a text file. Experimental data from Dipanjana Saha.

# In[1]:


import pandas as pd
import numpy as np
import codecs
import matplotlib.pyplot as plt

# get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


file_name = 'step0.txt'
file_path = '/Users/sharbatc/Downloads/'+file_name #replace with own filepath

with codecs.open(file_path,'r', encoding='utf-8',errors='ignore') as f: #ignore errors of encoding utf-8
    lines = f.readlines() #check file encoding errors


# In[3]:


beginning_value = [i for i in lines if i.startswith('Position X ROI#1')]
# print(beginning_value)


# In[4]:


list_start = [i for i, j in enumerate(lines) if j == beginning_value[0]] #array index having the value beginning_value (Position ...)
csv_list = lines[list_start[0]:]
csv_string = ''.join(csv_list)


# In[5]:


# show what the string looks like
# csv_string


# In[6]:


# make a list of lists, each list being at \r\n and within one list, values being separated by ,
data = list(map(lambda x: x.split(','),csv_string.split("\r\n")))


# In[7]:


data[:5]


# In[8]:


# remove the extra '' character at end of list by popping it away
for item in data[1:]:
    item.pop()


# In[9]:


# show what the final list looks like
data[:5]


# In[10]:


df = pd.DataFrame(data[1:], columns=data[0])
df.head()


# In[11]:


# convert all strings to numerics (float)
df = df.apply(pd.to_numeric)


# In[12]:


# preliminary statistics of the data
df.describe()


# In[18]:


intensity_x = df[' Intensity X ROI#1'].dropna()
intensity_y = df[' Intensity Y ROI#1'].dropna()

fig = plt.subplots()

plt.title(file_name)
plt.plot(intensity_x, label = 'Intensity X')
plt.plot(intensity_y, label = 'Intensity Y')
plt.xticks(np.arange(0, len(intensity_y), 250))
plt.yticks(np.arange(0, max(intensity_y), 2500))
plt.xlabel('Count')
plt.xticks(rotation=45)
plt.ylabel('Intensities')
plt.legend()
# plt.savefig('intensities_plot.jpeg')

plt.show()


# In[ ]:




