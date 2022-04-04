#!/usr/bin/env python
# coding: utf-8

# # **Análise Anual**

# ## AGV - Água Vermelha

# In[1]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=0)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
layout = go.Layout(title='Dados Anuais (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Anos'})

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
layout = go.Layout(title='Afluência Real por ano (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Anos'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## BAB - Barra Bonita

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=1)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
layout = go.Layout(title='Dados Anuais (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Anos'})

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
layout = go.Layout(title='Afluência Real por ano (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Anos'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## BAR - Bariri

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=2)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
layout = go.Layout(title='Dados Anuais (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Anos'})

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
layout = go.Layout(title='Afluência Real por ano (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Anos'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## CAC - Caconde

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=3)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)


# ## EUC - Euclides da Cunha

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=4)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)


# ## IBI - Ibitinga

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=5)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)


# ## LMO - Limoeiro

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=6)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
layout = go.Layout(title='Dados Anuais (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Anos'})

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
layout = go.Layout(title='Afluência Real por ano (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Anos'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## NVA - Nova Avanhandava

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=7)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)


# ## PRO - Promissão

# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=8)


# In[ ]:


vazao_df = pd.DataFrame
datas = []
qturb = []
qaflu = []
qvert = []
aflu_real = []

for i in range(1983, 2023):
  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()
  
  datas.append(str(i))

  qturb.append(qturb_verao)
  qaflu.append(qaflu_verao)
  qvert.append(qvert_verao)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)


# In[ ]:


turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = datas, y = qaflu, mode = 'lines', name = 'Afluente')
vertida = go.Scatter(x = datas, y = qvert, mode = 'lines', name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)

