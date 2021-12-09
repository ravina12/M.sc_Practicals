#!/usr/bin/env python
# coding: utf-8

# # practical1: data collection , modelling and compilation
# 

# In[3]:


my_dist = {'name':['a','b','c','d','e','f','g'],
            'age':[20,21,23,25,27,32,21],
             'designation':['vp','teacher','ca','engineer','developer','ceo','vp']}
import pandas as pd
import numpy as np

df-pd.DataFrame(my_dist)
df


# In[ ]:





# In[ ]:





# In[5]:


my_dist = {'name':['a','b','c','d','e','f','g'],
            'age':[20,21,23,25,27,32,21],
             'designation':['vp','teacher','ca','engineer','developer','ceo','vp']}
import pandas as pd
import numpy as np

df=pd.DataFrame(my_dist)
df


# In[6]:


df.to_csv('csv_fds')
df


# In[7]:


df_csv=pd.read_csv('csv_fds')
df_csv


# In[8]:


df.to_csv('csv_fds',index=False)
df_csv=pd.read_csv('csv_fds',)
df_csv


# In[10]:


import pandas as pd
Location = "C:/Users/HP/Downloads/student-mat.csv"
df = pd.read_csv(Location, header-None)
df.head()


# In[ ]:





# In[13]:


import pandas as pd
Location = "C:/Users/HP/Downloads/student-mat.csv"
df = pd.read_csv(Location, header=None)
df.head()


# In[14]:


import pandas as pd
names = ['bob','ravina','hina','krishna','ashu']
grades = [23,67,68,72,90]
bscdegress = [1,2,5,9,0]
mscdegrees = [9,2,7,12,5]
phddegress = [0,2,4,1,0]
Degrees=zip(names,grades,bscdegress,mscdegrees,phddegress)
columns = ['name','grades','bsc','msc','phd']
df = pd.DataFrame(data = Degrees , columns=columns)
df


# In[16]:


import pandas as pd
Location = "C:/Users/HP/Downloads/gradedata.xlsx"
df = pd.read_excel(Location)

df.columns=['first','last','new','grades','excer','hr','add','a']
df.head()


# In[17]:


import pandas as pd
names = ['bob','ravina','hina','krishna','ashu']
grades = [23,67,68,72,90]
Gradelist = zip(names,grades)
df = pd.DataFrame(data = Gradelist , columns = ['names','grades'])
writer = pd.ExcelWriter('dataframe.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='sheet1')
writer.save()


# In[19]:


import sqlite3
con = sqlite3.connect("C:/Users/HP/Downloads/portal_mammals.sqlite")
cur = con.cursor()
for row in cur.execute("SELECT * FROM species;"):
    print(row)
    
con.close()


# In[21]:


import sqlite3
con = sqlite3.connect("C:/Users/HP/Downloads/portal_mammals.sqlite")
cur = con.cursor()
cur.execute('SELECT plot_id FROM plots WHERE plot_type="Control"')
print(cur.fetchall())
cur.execute('SELECT species FROM species WHERE taxa="Bird"')
print(cur.fetchone())
con.close()


# Saving data to SQL
# 

# In[2]:


from pandas import DataFrame
Cars={'Brand':['audi','lamborgini','tata','motor'],
      'Price':[20000,50000,100000,404855]
     }
df=DataFrame(Cars,columns=['Brand','Price'])
print(df)


# In[3]:


import sqlite3


# In[4]:


conn=sqlite3.connect('TestDB1_fds.db')
c=conn.cursor()


# In[5]:


c.execute('CREATE TABLE Cars1_fds(Brand text,Price number)')
conn.commit()


# In[6]:


df.to_sql('CARS',conn,if_exists='replace',index=False)


# In[8]:


c.execute('''
SELECT Brand,max(price) from CARS
''')


# In[9]:


df=DataFrame(c.fetchall(),columns=['Brands','Price'])
df


# In[ ]:




