
# coding: utf-8

# In[4]:

import csv

durations = []
filename='small.csv'
with open(filename, 'r') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    header = next(filereader)
    for row in filereader:
        durations.append(int(row[0]))
        
print(durations)


# In[5]:

import pandas as pd

filename='small.csv'
df=pd.read_csv(filename, sep=',')
print (df)


# In[6]:

df.columns


# In[7]:

df.head()


# In[8]:

df.tail()


# In[9]:

df.tail(3)


# In[10]:

df.describe()


# In[ ]:

for index, row in df.iterrows():
    print(index, row['starttime'])


# In[ ]:

import pandas as pd

filename='small.csv'
df=pd.read_csv(filename, sep=',')
print (df)

#for index, row in df.iterrows():
#    print(index, row['birth year'])


# In[ ]:




# In[28]:

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

filename='201601-citibike-tripdata.csv'
df=pd.read_csv(filename, sep=',')
#print (df)


# In[32]:

import math
MAX_AGE = 100

ages = []
now = dt.datetime.now()
this_year = now.year

for index, row in df.iterrows():
    birth_year = row['birth year']
    if (math.isnan(birth_year) == False):
        age = this_year - int(birth_year)
        if (age <= MAX_AGE):
            ages.append(this_year - int(birth_year))


# In[33]:

print(ages)


# In[41]:


#counts = {}
#uniqueages = set(ages)
#for age in uniqueages:
#    counts[age] = ages.count(age)

plt.hist(ages, bins=25)
plt.show()


# In[ ]:



