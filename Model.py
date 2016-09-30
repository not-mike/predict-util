
# coding: utf-8

# In[6]:

get_ipython().magic(u'matplotlib inline')

# Imports
import time
import numpy as np
import scipy.stats as stats

import Gambler
import eventGenerator as eg

import matplotlib.pyplot as plt

# Import widget methods
from IPython.html.widgets import *


# In[9]:

class model(object):
    
    def __init__(self, numAgents = 100):
        self.agents = []
        self.event = eg.randomBinary()
        for i in range(numAgents):
            self.agents.append(Gambler.Gambler())


# In[38]:

M = model()
# This doesn't do what I want, which is to see the __str__ for each agent in the list.
for i in range(len(M.agents)):
    print str(M.agents[i])


# In[ ]:




# In[ ]:



