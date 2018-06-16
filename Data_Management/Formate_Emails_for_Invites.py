
# coding: utf-8

# In[2]:



from pymongo import MongoClient
import pymongo
import numpy as np
import pickle


# In[3]:


client = MongoClient()
print (client)


# In[4]:


db = client.Trai
db


# In[7]:


emails =[]


# In[8]:


for a in db.Trai.find({"email":{'$regex': '.*@gmail\.com$'}}):
    emails.append(a[u'email'])


# In[11]:


#store all in pickel databse

with open('/home/sudhanshu/Github/G_Emials.pkl','wb') as db:
    pickle.dump(emails, db)
    
# gmail email ids are dumpled as list 

