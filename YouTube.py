
# coding: utf-8

# In[80]:


import pandas as pd
import numpy as np
import json


# In[81]:


ca_yet_df = pd.read_csv('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/CAvideos.csv')
de_yet_df= pd.read_csv('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/DEvideos.csv')
fr_yet_df= pd.read_csv('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/FRvideos.csv')
gb_yet_df= pd.read_csv('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/GBvideos.csv')
in_yet_df= pd.read_csv('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/INvideos.csv')
us_yet_df= pd.read_csv('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/USvideos.csv')


# In[82]:



ca_yet_df.info()
#description has 1296 null value 

ca_yet_df.shape
#(40881, 16)


# In[83]:


ca_yet_df.head()


# In[84]:


ca_yet_df['country']='CA'
de_yet_df['country']='DE'
fr_yet_df['country']='FR'
gb_yet_df['country']='GB'
in_yet_df['country']='IN'
us_yet_df['country']='US'


# In[85]:


ca_yet_df['category_id']= ca_yet_df['category_id'].astype(str)
ca_category_id ={}
with open('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/CA_category_id.json', 'r') as f:
    data = json.load(f)
    for ca_category in data['items']:
        ca_category_id[ca_category['id']] = ca_category['snippet']['title']

ca_yet_df.insert(4, 'category', ca_yet_df['category_id'].map(ca_category_id))


# In[86]:


ca_yet_df


# In[87]:


us_yet_df['category_id']= us_yet_df['category_id'].astype(str)
us_category_id ={}
with open('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/US_category_id.json', 'r') as f:
    data = json.load(f)
    for us_category in data['items']:
        us_category_id[us_category['id']] = us_category['snippet']['title']

us_yet_df.insert(4, 'category', us_yet_df['category_id'].map(us_category_id))


# In[88]:


us_yet_df


# In[90]:


gb_yet_df['category_id']= gb_yet_df['category_id'].astype(str)
gb_category_id ={}
with open('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/GB_category_id.json', 'r') as f:
    data = json.load(f)
    for gb_category in data['items']:
        gb_category_id[gb_category['id']] = gb_category['snippet']['title']

gb_yet_df.insert(4, 'category', gb_yet_df['category_id'].map(gb_category_id))


# In[91]:


gb_yet_df


# In[92]:


de_yet_df['category_id']= de_yet_df['category_id'].astype(str)
de_category_id ={}
with open('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/DE_category_id.json', 'r') as f:
    data = json.load(f)
    for de_category in data['items']:
        de_category_id[de_category['id']] = de_category['snippet']['title']

de_yet_df.insert(4, 'category', de_yet_df['category_id'].map(de_category_id))


# In[93]:


de_yet_df


# In[94]:


fr_yet_df['category_id']= fr_yet_df['category_id'].astype(str)
fr_category_id ={}
with open('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/FR_category_id.json', 'r') as f:
    data = json.load(f)
    for fr_category in data['items']:
        fr_category_id[fr_category['id']] = fr_category['snippet']['title']

fr_yet_df.insert(4, 'category', fr_yet_df['category_id'].map(fr_category_id))


# In[95]:


fr_yet_df


# In[96]:


in_yet_df['category_id']= in_yet_df['category_id'].astype(str)
in_category_id ={}
with open('D:/DataScienceFoundation/SpringBoard/YouTube Project/youtube-new/IN_category_id.json', 'r') as f:
    data = json.load(f)
    for in_category in data['items']:
        in_category_id[in_category['id']] = in_category['snippet']['title']

in_yet_df.insert(4, 'category', in_yet_df['category_id'].map(in_category_id))


# In[97]:


in_yet_df


# In[98]:


df_videos = pd.concat([ca_yet_df, de_yet_df, fr_yet_df, gb_yet_df, in_yet_df, us_yet_df])


# In[99]:


df_videos['category'].unique()


# In[33]:


df_videos.count()


# In[34]:


df_videos['trending_date'] = pd.to_datetime(df_videos['trending_date'],errors='coerce', format='%y.%d.%m')


# In[35]:


df_videos['publish_time'] = pd.to_datetime(df_videos['publish_time'], errors='coerce', format='%Y-%m-%dT%H:%M:%S.%fZ')


# In[36]:


df_videos.head()


# In[37]:


df_videos = df_videos.reset_index().set_index('video_id')


# In[104]:


df_videos[df_videos['country']=='CA'].head()


# In[117]:


df_videos_grp_cntry = df_videos.groupby(['video_id','country']).count()['title'].sort_values(ascending=False)
df_videos_grp_cntry.head()


# In[118]:


df_videos_grp_cntry.tail()

