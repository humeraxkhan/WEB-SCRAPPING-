#!/usr/bin/env python
# coding: utf-8

# In[30]:


from bs4 import BeautifulSoup
import requests


# In[31]:


url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[32]:


print(soup)


# In[33]:


soup.find('table')


# In[66]:


soup.find('table',class_ = 'wikitable sortable jquery-tablesorter')


# In[67]:


table = soup.find_all('table')[1]


# In[74]:


print(table)


# In[68]:


world_titles= table.find_all('th')


# In[69]:


world_tables_titles= [title.text.strip() for  title in world_titles ]
print(world_tables_titles)


# In[70]:


import pandas as pd


# In[71]:


df = pd.DataFrame(columns = world_tables_titles) 
df


# In[72]:


column_data = table.find_all('tr')


# In[75]:


for row in column_data:
    
    row_data = row.find_all('td')
    individuals_row_data = [data.text.strip() for  data in row_data ]
    print(individuals_row_data)


# In[79]:


for row in column_data[1:]:
    
    row_data = row.find_all('td')
    individuals_row_data = [data.text.strip() for  data in row_data ]
    print(individuals_row_data)
    
    length = len(df)
    df.loc[length] = individuals_row_data
    


# In[80]:


df


# In[82]:


df.to_csv(r'C:\Users\DELL\OneDrive\Documents\Companies.csv',index = False )


# In[ ]:




