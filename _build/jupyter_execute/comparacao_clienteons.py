#!/usr/bin/env python
# coding: utf-8

# # **Comparação entre os dados do cliente e da ONS**

# ## AGV - Água Vermelha

# In[1]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=0)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_agv.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## BAB - Barra Bonita

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=1)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_bab.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## BAR - Bariri

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=2)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_bar.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## CAC - Caconde

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=3)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_cac.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## EUC - Euclides da Cunha

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=4)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_euc.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## IBI - Ibitinga

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=5)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_ibi.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## LMO - Limoeiro

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=6)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_lmo.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## NVA - Nova Avanhandava

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=7)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_nva.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## PRO - Promissão

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=8)
base_ons = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Turbinada Hidreletricas ONS/turbinada_pro.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
geracao = go.Scatter(x = base_ons['DATA'], y = base_ons['TURBINADA'], mode = 'lines', name = 'Turbinada ONS')
data = [turbinada, geracao]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

