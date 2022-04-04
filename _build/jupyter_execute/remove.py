#!/usr/bin/env python
# coding: utf-8

# ## AGV - Água Vermelha

# In[1]:


import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("projeto_aes/*.ipynb", recursive=True)

# Text to look for in adding tags
text_search_dict = {
    "# NO CODE": "remove-input",  # Remove only the input
}

# Search through each notebook and look for the text, add a tag if necessary
for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        cell_tags = cell.get('metadata', {}).get('tags', [])
        for key, val in text_search_dict.items():
            if key in cell['source']:
                if val not in cell_tags:
                    cell_tags.append(val)
        if len(cell_tags) > 0:
            cell['metadata']['tags'] = cell_tags

    nbf.write(ntbk, ipath)

print('Foi certo')


# In[2]:


import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("projeto_aes/*.ipynb", recursive=True)

# Text to look for in adding tags
text_search_dict = {
    "# HIDDEN": "remove-cell",  # Remove the whole cell
    "# NO CODE": "remove-input",  # Remove only the input
    "# HIDE CODE": "hide-input"  # Hide the input w/ a button to show
}

# Search through each notebook and look for the text, add a tag if necessary
for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        cell_tags = cell.get('metadata', {}).get('tags', [])
        for key, val in text_search_dict.items():
            if key in cell['source']:
                if val not in cell_tags:
                    cell_tags.append(val)
        if len(cell_tags) > 0:
            cell['metadata']['tags'] = cell_tags

    nbf.write(ntbk, ipath)


# In[3]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=1)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=2)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=3)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=4)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=5)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=6)


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


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=7)


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


# In[ ]:


base = pd.read_excel('/content/drive/MyDrive/ENACOM/Projeto AES/BDHE_1983 a 2022.xlsx', sheet_name=8)


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

