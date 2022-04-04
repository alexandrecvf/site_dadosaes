#!/usr/bin/env python
# coding: utf-8

# # **Análise Anual (sem médias)**

# ## **AGV - Água Vermelha**

# In[1]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=0)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=1)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=2)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=3)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=4)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=5)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=6)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=7)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=8)


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

