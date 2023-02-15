#!/usr/bin/env python
# coding: utf-8

# ## Step 1: Import libraries: pandas and seaborn

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# ## Step 2: Read Data

# In[2]:


sal = pd.read_csv(r"C:\Users\pdhotre\Desktop\CIS 508 Data Mining\Github\Salaries.csv")


# In[3]:


sal.head()


# ## Q1: How many columns and rows are there in the dataset?

# In[4]:


sal.shape


# ## Q2: What the average of total pay ['TotalPay'] of San Francisco’s city employees?

# In[5]:


sal.describe().mean()


# ## OR

# In[6]:


sal["TotalPay"].mean()


# ## Q3: What is the maximum benefit received by a city employee?

# In[7]:


sal['Benefits'].max()


# ## Q4: How much benefits did JOSEPH DRISCOLL receive?

# In[8]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# ## Q5: What is the average ’total benefits’ received by Special Nurse?

# In[9]:


sal[sal['JobTitle']=='Special Nurse']['TotalPayBenefits'].mean()


# ## Q6: What is the name of the employee in the 3500th record?

# In[10]:


sal.iloc[3499]


# ## Q7: How many missing values does variable 'BasePay' have?

# In[11]:


sal.isnull().sum()


# ## Q8: Create a boxplot of TotalPay variable across different job status (Status).

# In[12]:


sns.boxplot(x='TotalPay',y='Status',data=sal)


# ## Q9: Create a boxplot of BasePay variable across different years (Year variable).

# In[13]:


sns.boxplot(x=sal['Year'],y=sal['BasePay'])


# ## Q10: Create a histogram for TotalPay variable

# In[14]:


sns.histplot(sal['TotalPay'])


# In[ ]:




