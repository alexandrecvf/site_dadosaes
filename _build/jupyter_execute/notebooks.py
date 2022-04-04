#!/usr/bin/env python
# coding: utf-8

# # **Imports**

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as py
from datetime import datetime


# # **Estações x Vazão**

# ## **AGV - Água Vermelha**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=0)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=1)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=2)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=3)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=4)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=5)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=6)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=7)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=8)


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


# # **Análise Anual**

# ## AGV - Água Vermelha

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=0)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=1)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=2)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=3)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=4)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=5)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=6)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=7)


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=8)


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


# # **Análise de 5 anos**

# ## AGV - Água Vermelha

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=0)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2018 a 2022 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1983 a 1987 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1988 a 1992 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1993 a 1997 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1998 a 2002 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2003 a 2007 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2008 a 2012 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2013 a 2017 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2018 a 2022 (Água Vermelha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## BAB - Barra Bonita

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=1)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2018 a 2022 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1983 a 1987 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1988 a 1992 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1993 a 1997 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1998 a 2002 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2003 a 2007 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2008 a 2012 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2013 a 2017 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2018 a 2022 (Barra Bonita)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## BAR - Bariri

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=2)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
fig = go.Figure(data=data, layout=layout)
layout = go.Layout(title='Vazão de 2018 a 2022 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1983 a 1987 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1988 a 1992 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1993 a 1997 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 1998 a 2002 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2003 a 2007 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2008 a 2012 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2013 a 2017 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
layout = go.Layout(title='Vazão de 2018 a 2022 (Bariri)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## CAC - Caconde

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=3)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2018 a 2022 (Caconde)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)


# ## EUC - Euclides da Cunha

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=4)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2018 a 2022 (Euclides da Cunha)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)


# ## IBI - Ibitinga

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=5)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2018 a 2022 (Ibitinga)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)


# ## LMO - Limoeiro

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=6)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2018 a 2022 (Limoeiro)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)


# ## NVA - Nova Avanhandava

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=7)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2018 a 2022 (Nova Avanhandava)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)


# ## PRO - Promissão

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=8)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1983-01-01') & (base['DATA'] <= '1987-12-31')
df_83_87 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1988-01-01') & (base['DATA'] <= '1992-12-31')
df_88_92 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1993-01-01') & (base['DATA'] <= '1997-12-31')
df_93_97 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '1998-01-01') & (base['DATA'] <= '2002-12-31')
df_98_02 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2003-01-01') & (base['DATA'] <= '2007-12-31')
df_03_07 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2008-01-01') & (base['DATA'] <= '2012-12-31')
df_08_12 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2013-01-01') & (base['DATA'] <= '2017-12-31')
df_13_17 = base[selecao]

base['DATA'] = pd.to_datetime(base['DATA'])
selecao = (base['DATA'] >= '2018-01-01') & (base['DATA'] <= '2022-12-31')
df_18_22 = base[selecao]


# In[ ]:


turbinada = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_83_87['DATA'], y = df_83_87['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1983 a 1987 (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_88_92['DATA'], y = df_88_92['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1988 a 1992 (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_93_97['DATA'], y = df_93_97['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1993 a 1997 (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_98_02['DATA'], y = df_98_02['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 1998 a 2002 (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_03_07['DATA'], y = df_03_07['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2003 a 2007 (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_08_12['DATA'], y = df_08_12['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2008 a 2012 (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_13_17['DATA'], y = df_13_17['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2013 a 2017 (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

turbinada = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QTURB_MED'], mode = 'lines', name = 'Turbinada')
afluente = go.Scatter(x = df_18_22['DATA'], y = df_18_22['QAFLU_MED'], mode = 'lines', name = 'Afluente')
data = [turbinada, afluente]
layout = go.Layout(title='Vazão de 2018 a 2022 (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:


afluencia_real = go.Scatter(x = df_83_87['DATA'],
                    y = df_83_87['QTURB_MED']+df_83_87['QAFLU_MED']+df_83_87['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_88_92['DATA'],
                    y = df_88_92['QTURB_MED']+df_88_92['QAFLU_MED']+df_88_92['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_93_97['DATA'],
                    y = df_93_97['QTURB_MED']+df_93_97['QAFLU_MED']+df_93_97['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_98_02['DATA'],
                    y = df_98_02['QTURB_MED']+df_98_02['QAFLU_MED']+df_98_02['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_03_07['DATA'],
                    y = df_03_07['QTURB_MED']+df_03_07['QAFLU_MED']+df_03_07['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_08_12['DATA'],
                    y = df_08_12['QTURB_MED']+df_08_12['QAFLU_MED']+df_08_12['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_13_17['DATA'],
                    y = df_13_17['QTURB_MED']+df_13_17['QAFLU_MED']+df_13_17['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)

afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real')
data = [afluencia_real]
py.iplot(data)


# # **Comparação entre os dados do cliente e da ONS**

# ## AGV - Água Vermelha

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=0)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_agv.xlsx')


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=1)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_bab.xlsx')


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=2)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_bar.xlsx')


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=3)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_cac.xlsx')


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=4)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_euc.xlsx')


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=5)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_ibi.xlsx')


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=6)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_lmo.xlsx')


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=7)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_nva.xlsx')


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


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=8)
base_ons = pd.read_excel('Turbinada Hidreletricas ONS/turbinada_pro.xlsx')


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


# In[ ]:


afluencia_real = go.Scatter(x = df_18_22['DATA'],
                    y = df_18_22['QTURB_MED']+df_18_22['QAFLU_MED']+df_18_22['QVERT_MED'],
                    mode = 'lines',
                    name = 'Afluência Real (m³/s)')
data = [afluencia_real, geracao, turbinada]
layout = go.Layout(title='Comparação entre os dados do cliente e da ONS nos últimos 5 anos (Promissão)',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# # **Análise Anual (sem médias)**

# ## **AGV - Água Vermelha**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=0)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Água Vermelha de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Água Vermelha de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Água Vermelha de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Água Vermelha de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Água Vermelha de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **BAB - Barra Bonita**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=1)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Barra Bonita de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Barra Bonita de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Barra Bonita de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Barra Bonita de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Barra Bonita de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **BAR - Bariri**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=2)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Bariri de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Bariri de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Bariri de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Bariri de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Bariri de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **CAC - Caconde**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=3)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Caconde de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Caconde de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Caconde de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Caconde de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Caconde de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **EUC - Euclides da Cunha**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=4)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Euclides da Cunha de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Euclides da Cunha de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Euclides da Cunha de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Euclides da Cunha de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Euclides da Cunha de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **IBI - Ibitinga**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=5)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Ibitinga de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Ibitinga de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Ibitinga de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Ibitinga de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Ibitinga de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **LMO - Limoeiro**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=6)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Limoeiro de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Limoeiro de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Limoeiro de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Limoeiro de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Limoeiro de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **NVA - Nova Avanhandava**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=7)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Nova Avanhandava de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Nova Avanhandava de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Nova Avanhandava de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Nova Avanhandava de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Nova Avanhandava de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **PRO - Promissão**

# In[ ]:


base = pd.read_excel('BDHE_1983 a 2022.xlsx', sheet_name=8)


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
dias_ano = []

for i in range(1,366):
  dias_ano.append(i)

for i in range(1997, 2023):
  selecao = (base['DATA'] >= str(i)+'-01-01') & (base['DATA'] <= str(i)+'-12-31')
  df = base[selecao]

  globals()['df_%s' % i] = base[selecao]

  globals()['turb_%s' % i] = go.Scatter(x = dias_ano, y = globals()['df_%s' % i]['QTURB_MED'], mode = 'lines', name = str(i))

data = [turb_1997,turb_1998,turb_1999,turb_2000,turb_2001]
layout = go.Layout(title='Vazão da Usina Promissão de 1997 a 2001',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2002,turb_2003,turb_2004,turb_2005,turb_2006]
layout = go.Layout(title='Vazão da Usina Promissão de 2002 a 2006',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2007,turb_2008,turb_2009,turb_2010,turb_2011]
layout = go.Layout(title='Vazão da Usina Promissão de 2008 a 2011',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2012,turb_2013,turb_2014,turb_2015,turb_2016]
layout = go.Layout(title='Vazão da Usina Promissão de 2012 a 2016',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data = [turb_2017,turb_2018,turb_2019,turb_2020,turb_2021]
layout = go.Layout(title='Vazão da Usina Promissão de 2017 a 2021',
                   yaxis={'title':'Vazão (m³/s)'},
                   xaxis={'title':'Dias do Ano'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# # **Análise Anual (com horário)**

# ## **Solar**

# ### **Guaimbé**

# In[ ]:


base = pd.read_excel('Geração Solar ONS/geracao_guaimbe.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(5, 20):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Guaimbé em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Boa Hora**

# In[ ]:


base = pd.read_excel('Geração Solar ONS/geracao_boahora.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(5, 20):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Boa Hora em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ## **Eólica**

# ### **Araças**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_aracas.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Boa Hora em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Areia Branca**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_areiabranca.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Areia Branca em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Caetité**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_caetite.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Caetite em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Icaraí**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_icarai.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Icaraí em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Miassaba 3**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_miassaba_3.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Miassaba 3 em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Morrão**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_morrao.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Morrão em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Pelourinho**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_pelourinho.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina de Pelourinho em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Rei dos Ventos 1**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_reidosventos_1.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina Rei dos Ventos 1 em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# ### **Rei dos Ventos 3**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_reidosventos_3.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
qturb = []
teste = 0

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 25):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          qturb.append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

  turbinada = go.Scatter(x = datas, y = qturb, mode = 'lines', name = 'Turbinada')
  data = [turbinada]
  layout = go.Layout(title=f'Energia Gerada pela Usina Rei dos Ventos 3 em {ano} ',
                    yaxis={'title':'Geração (MWmed)'},
                    xaxis={'title':'Dias do Ano'})
  fig = go.Figure(data=data, layout=layout)
  py.iplot(fig)

  datas = []
  qturb = []


# 

# # **Análise Horária**

# ## **Solar**

# ### **Guaimbé**

# In[ ]:


base = pd.read_excel('Geração Solar ONS/geracao_guaimbe.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias = []
medias_datas = []

for i in range(5, 21):
  globals()['qturb_%s' % i] = []

for ano in range(2018,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(5, 21):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(5, 21):
  medias.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title=f'Média da Energia Gerada pela Usina de Guaimbé por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Boa Hora**

# In[ ]:


base = pd.read_excel('Geração Solar ONS/geracao_boahora.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias = []
medias_datas = []

for i in range(5, 21):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(5, 21):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(5, 21):
  medias.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title=f'Média da Energia Gerada pela Usina de Boa Hora por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## **Eólica**

# ### **Araçás**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_aracas.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_aracas = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_aracas.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_aracas, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Araçás por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Areia Branca**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_areiabranca.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_areiabranca = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_areiabranca.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_areiabranca, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Areia Branca por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Caetité**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_caetite.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_caetite = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_caetite.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_caetite, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Caetité por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Icaraí**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_icarai.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_icarai = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_icarai.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_icarai, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Icaraí por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Miassaba 3**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_miassaba_3.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_miassaba = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_miassaba.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_miassaba, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Miassaba 3 por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Morrão**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_morrao.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_morrao = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_morrao.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_morrao, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Morrão por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Pelourinho**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_pelourinho.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_pelourinho = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_pelourinho.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_pelourinho, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Pelourinho por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Rei dos Ventos 1**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_reidosventos_1.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_reidosventos1 = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_reidosventos1.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_reidosventos1, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Rei dos Ventos 1 por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ### **Rei dos Ventos 3**

# In[ ]:


base = pd.read_excel('Geração Eolica ONS/geracao_reidosventos_3.xlsx')


# In[ ]:


base['DATA'] = pd.to_datetime(base['DATA'])
datas = []
teste = 0
medias_reidosventos3 = []
medias_datas = []

for i in range(0, 24):
  globals()['qturb_%s' % i] = []

for ano in range(2019,2023):
  for mes in range(1,13):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
      qtddias = 32
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
      qtddias = 31
    elif mes == 2:
      qtddias = 29
    
    for dia in range(1,qtddias):
      for i in range(0, 24):
        try:
          selecao = (base['DATA'] >= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00') & (base['DATA'] <= str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
          df_verao = base[selecao]
          qturb_verao = df_verao['GERACAO']
          globals()['qturb_%s' % i].append(float(qturb_verao.values))
          datas.append(str(ano)+'-'+str(mes)+'-'+str(dia)+' '+str(i)+':00')
        except:
          teste += 1 

for i in range(0, 24):
  medias_reidosventos3.append(np.mean(globals()['qturb_%s' % i]))
  medias_datas.append(str(i)+':00')

turbinada = go.Scatter(x = medias_datas, y = medias_reidosventos3, mode = 'lines', name = 'Turbinada')
data = [turbinada]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Rei dos Ventos 3 por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# ## Comparativo 

# In[ ]:


aracas = go.Scatter(x = medias_datas, y = medias_reidosventos3, mode = 'lines', name = 'Araçás')
areiabranca = go.Scatter(x = medias_datas, y = medias_areiabranca, mode = 'lines', name = 'Areia Branca')
caetite = go.Scatter(x = medias_datas, y = medias_caetite, mode = 'lines', name = 'Caetité')
icarai = go.Scatter(x = medias_datas, y = medias_icarai, mode = 'lines', name = 'Icaraí')
miassaba3 = go.Scatter(x = medias_datas, y = medias_miassaba, mode = 'lines', name = 'Miassaba 3')
morrao = go.Scatter(x = medias_datas, y = medias_morrao, mode = 'lines', name = 'Morrão')
pelourinho = go.Scatter(x = medias_datas, y = medias_pelourinho, mode = 'lines', name = 'Pelourinho')
reidosventos1 = go.Scatter(x = medias_datas, y = medias_reidosventos1, mode = 'lines', name = 'Rei dos Ventos 1')
reidosventos3 = go.Scatter(x = medias_datas, y = medias_reidosventos3, mode = 'lines', name = 'Rei dos Ventos 3')

data = [aracas, areiabranca, caetite, icarai, miassaba3, morrao, pelourinho, reidosventos1, reidosventos3]
layout = go.Layout(title='Média da Energia Gerada pela Usina de Rei dos Ventos 3 por Hora',
                  yaxis={'title':'Geração (MWmed)'},
                  xaxis={'title':'Horas'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

