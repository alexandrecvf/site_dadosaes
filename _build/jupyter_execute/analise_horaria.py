#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # **Análise Horária**

# ## **Solar**

# ### **Guaimbé**

# In[1]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Solar ONS/geracao_guaimbe.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Solar ONS/geracao_boahora.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_aracas.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_areiabranca.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_caetite.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_icarai.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_miassaba_3.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_morrao.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_pelourinho.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_reidosventos_1.xlsx')


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/Geração Eolica ONS/geracao_reidosventos_3.xlsx')


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


# ## **Comparativo**

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

