#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import os
import json
with open('./draft_content.json') as f:
    data = f.readline()
    spam_word = pd.read_csv('./spam_word.txt', header = None)
#     print(data)


# In[15]:


spam_word[0] = spam_word[0].apply(lambda x: x.split(" "))


# In[16]:


spam_word_list = list(spam_word[0][0])
spam_word_list


# In[17]:


for i in range(len(spam_word_list)):
    data = data.replace(spam_word_list[i], "")


# In[18]:


if not os.path.exists('new'):
    os.mkdir("new")


# In[20]:


with open('./new/draft_content.json', 'w') as f:
    f.write(data)


# In[ ]:





# In[ ]:




