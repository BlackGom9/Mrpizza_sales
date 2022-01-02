#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


mrpi_d = pd.read_excel("C:/Users/Kimkangmin/Desktop/mrpi/상계20년 1월 영업일보.xlsx", sheet_name = '영업일보 일일매출', header = 0) 
# 데이터를 변수에 저장


# In[3]:


mrpi_d


# In[4]:


mrpi_d = mrpi_d.T


# In[6]:


mrpi_d = mrpi_d.reset_index()


# In[8]:


mrpi_d = mrpi_d.rename(columns = {'index' : 'day', 0 : 'dayw', 1 : 'T_s', 2 : 'd_s', 3 : 'v_s', 4 : 'wea', 5 : 'T_l', 6 : 'T_r', 7 : 'B_p', 8 : 'B_l', 9 : 'B_r'})
# 날짜 = day, 요일 = dayw(day of week), 총 매출 = T_s(total sales), 배달총매출 = d_s(delivery sales), 내점 = v_s(visit sales), 날씨 = weather(wea), 총 사용한 라지 = T_l(total large), 총 사용한 레귤러 = T_r(total regular), 총 뷔페인원 = B_p(buffet people), 뷔페L = B_l(buffet large), 뷔페R = B_r(buffet regualr) 


# In[10]:


mrpi_d = mrpi_d.drop(0, axis = 0)


# In[11]:


mrpi_d


# In[ ]:




