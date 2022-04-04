#!/usr/bin/env python
# coding: utf-8

# # **Análise Anual (com horário)**

# ## **Solar**

# ### **Guaimbé**

# In[1]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Solar ONS/geracao_guaimbe.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Solar ONS/geracao_boahora.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_aracas.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_areiabranca.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_caetite.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_icarai.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_miassaba_3.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_morrao.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_pelourinho.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_reidosventos_1.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_reidosventos_3.xlsx')


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
