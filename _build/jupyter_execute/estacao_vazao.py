#!/usr/bin/env python
# coding: utf-8

# # **Estações x Vazão**

# ## **AGV - Água Vermelha**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]

# Criando Layout
layout = go.Layout(title='Vazão por estação do ano (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Estações do ano'})

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
layout = go.Layout(title=f'Afluência real (Água Vermelha) ',
                  yaxis={'title':'Vazão (m³/s)'},
                  xaxis={'title':'Estações do ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **BAB - Barra Bonita**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)

  '''colnames = ['Tipo']
  vazao_df = pd.DataFrame([[i, 'Verão', qturb_verao, qaflu_verao, qvert_verao],
                          [i, 'Outono', qturb_outono, qaflu_outono, qvert_outono],
                          [i, 'Inverno', qturb_inverno, qaflu_inverno, qvert_inverno],
                          [i, 'Primavera', qturb_primavera, qaflu_primavera, qvert_primavera]], columns = colnames)
  vazao_df.insert(1, "Verão"+str(i), qturb_verao, allow_duplicates=False)
  vazao_df.set_index('Tipo', inplace = True)'''


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]
# Criando Layout
layout = go.Layout(title='Vazão por estação do ano (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Estações do ano'})

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
# Criando Layout
layout = go.Layout(title='Afluência Real por estação do ano (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Estações do ano'})

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)


# ## **BAR - Bariri**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]
# Criando Layout
layout = go.Layout(title='Vazão por estação do ano (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Estações do ano'})

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
# Criando Layout
layout = go.Layout(title='Afluência Real por estação do ano (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Estações do ano'})

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)


# ## **CAC - Caconde**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)

  '''colnames = ['Tipo']
  vazao_df = pd.DataFrame([[i, 'Verão', qturb_verao, qaflu_verao, qvert_verao],
                          [i, 'Outono', qturb_outono, qaflu_outono, qvert_outono],
                          [i, 'Inverno', qturb_inverno, qaflu_inverno, qvert_inverno],
                          [i, 'Primavera', qturb_primavera, qaflu_primavera, qvert_primavera]], columns = colnames)
  vazao_df.insert(1, "Verão"+str(i), qturb_verao, allow_duplicates=False)
  vazao_df.set_index('Tipo', inplace = True)'''


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)


# ## **EUC - Euclides da Cunha**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)

  '''colnames = ['Tipo']
  vazao_df = pd.DataFrame([[i, 'Verão', qturb_verao, qaflu_verao, qvert_verao],
                          [i, 'Outono', qturb_outono, qaflu_outono, qvert_outono],
                          [i, 'Inverno', qturb_inverno, qaflu_inverno, qvert_inverno],
                          [i, 'Primavera', qturb_primavera, qaflu_primavera, qvert_primavera]], columns = colnames)
  vazao_df.insert(1, "Verão"+str(i), qturb_verao, allow_duplicates=False)
  vazao_df.set_index('Tipo', inplace = True)'''


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)


# ## **IBI - Ibitinga**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)

  '''colnames = ['Tipo']
  vazao_df = pd.DataFrame([[i, 'Verão', qturb_verao, qaflu_verao, qvert_verao],
                          [i, 'Outono', qturb_outono, qaflu_outono, qvert_outono],
                          [i, 'Inverno', qturb_inverno, qaflu_inverno, qvert_inverno],
                          [i, 'Primavera', qturb_primavera, qaflu_primavera, qvert_primavera]], columns = colnames)
  vazao_df.insert(1, "Verão"+str(i), qturb_verao, allow_duplicates=False)
  vazao_df.set_index('Tipo', inplace = True)'''


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)


# ## **LMO - Limoeiro**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]
# Criando Layout
layout = go.Layout(title='Vazão por estação do ano (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Estações do ano'})

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
# Criando Layout
layout = go.Layout(title='Afluência Real por estação do ano (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Estações do ano'})

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)


# ## **NAV - Nova Avanhandava**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)

  '''colnames = ['Tipo']
  vazao_df = pd.DataFrame([[i, 'Verão', qturb_verao, qaflu_verao, qvert_verao],
                          [i, 'Outono', qturb_outono, qaflu_outono, qvert_outono],
                          [i, 'Inverno', qturb_inverno, qaflu_inverno, qvert_inverno],
                          [i, 'Primavera', qturb_primavera, qaflu_primavera, qvert_primavera]], columns = colnames)
  vazao_df.insert(1, "Verão"+str(i), qturb_verao, allow_duplicates=False)
  vazao_df.set_index('Tipo', inplace = True)'''


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)


# ## **PRO - Promissão**

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
  selecao = (base['DATA'] >= str((i-1))+'-12-22') & (base['DATA'] <= str(i)+'-03-20')
  df_verao = base[selecao]
  qturb_verao = df_verao['QTURB_MED'].mean()
  qaflu_verao = df_verao['QAFLU_MED'].mean()
  qvert_verao = df_verao['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-03-21') & (base['DATA'] <= str(i)+'-06-21')
  df_outono = base[selecao]
  qturb_outono = df_outono['QTURB_MED'].mean()
  qaflu_outono = df_outono['QAFLU_MED'].mean()
  qvert_outono = df_outono['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-06-22') & (base['DATA'] <= str(i)+'-09-22')
  df_inverno = base[selecao]
  qturb_inverno = df_inverno['QTURB_MED'].mean()
  qaflu_inverno = df_inverno['QAFLU_MED'].mean()
  qvert_inverno = df_inverno['QVERT_MED'].mean()

  base['DATA'] = pd.to_datetime(base['DATA'])
  selecao = (base['DATA'] >= str(i)+'-09-23') & (base['DATA'] <= str(i)+'-12-22')
  df_primavera = base[selecao]
  qturb_primavera = df_primavera['QTURB_MED'].mean()
  qaflu_primavera = df_primavera['QAFLU_MED'].mean()
  qvert_primavera = df_primavera['QVERT_MED'].mean()
  
  datas.append('Ver-'+str(i))
  datas.append('Out-'+str(i))
  datas.append('Inv-'+str(i))
  datas.append('Pri-'+str(i))

  qturb.append(qturb_verao)
  qturb.append(qturb_outono)
  qturb.append(qturb_inverno)
  qturb.append(qturb_primavera)

  qaflu.append(qaflu_verao)
  qaflu.append(qaflu_outono)
  qaflu.append(qaflu_inverno)
  qaflu.append(qaflu_primavera)

  qvert.append(qvert_verao)
  qvert.append(qvert_outono)
  qvert.append(qvert_inverno)
  qvert.append(qvert_primavera)

  aflu_real.append(qturb_verao+qaflu_verao+qvert_verao)
  aflu_real.append(qturb_outono+qaflu_outono+qvert_outono)
  aflu_real.append(qturb_inverno+qaflu_inverno+qvert_inverno)
  aflu_real.append(qturb_primavera+qaflu_primavera+qvert_primavera)

  '''colnames = ['Tipo']
  vazao_df = pd.DataFrame([[i, 'Verão', qturb_verao, qaflu_verao, qvert_verao],
                          [i, 'Outono', qturb_outono, qaflu_outono, qvert_outono],
                          [i, 'Inverno', qturb_inverno, qaflu_inverno, qvert_inverno],
                          [i, 'Primavera', qturb_primavera, qaflu_primavera, qvert_primavera]], columns = colnames)
  vazao_df.insert(1, "Verão"+str(i), qturb_verao, allow_duplicates=False)
  vazao_df.set_index('Tipo', inplace = True)'''


# In[ ]:


turbinada = go.Scatter(x = datas,
                    y = qturb,
                    mode = 'lines',
                    name = 'Turbinada')

afluente = go.Scatter(x = datas,
                    y = qaflu,
                    mode = 'lines',
                    name = 'Afluente')

vertida = go.Scatter(x = datas,
                    y = qvert,
                    mode = 'lines',
                    name = 'Vertida')

data = [turbinada, afluente, vertida]
py.iplot(data)


# In[ ]:


afluencia_real = go.Scatter(x = datas,
                    y = aflu_real,
                    mode = 'lines',
                    name = 'Afluência Real')

data = [afluencia_real]
py.iplot(data)

