#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1w3TmCcQPoc7ew1CXmwwEUpWeHJzJQqGZ?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[1]:


# Passo 1: importar a base de dados
import pandas as pd


# In[2]:


# Passo 2: visualizar a base de dados para entender os dados
tabela_clientes = pd.read_csv(r'C:\Users\Virtual Office\Python\Módulo 49 - intensivão de Python\Aula 2\telecom_users.csv')
display(tabela_clientes)


# In[3]:


# Verificando a quantidade de colunas que há na base de dados
display(tabela_clientes.columns)


# In[4]:


# Com esse comando consigo visualizar as informações gerais sobre os dados que constam na base de dados
display(tabela_clientes.info())
# Com esse comando consigo identificar a quantidade de valores nulos por coluna
display(tabela_clientes.isna().sum())


# In[5]:


# Passo 3: tratamento de dados
    # Convertendo os tipos de dados das colunas que carregam dados numericos, porém estão como tipo objet
tabela_clientes['TotalGasto'] = pd.to_numeric(tabela_clientes['TotalGasto'], errors = 'coerce')
    # Removendo a coluna Unnamed: 0, para construção da análise essa informa não é relevante
tabela_clientes = tabela_clientes.drop('Unnamed: 0',axis = 1)
    # Removendo as colunas que estão com todas as linhas vazias 
tabela_clientes = tabela_clientes.dropna(how = 'all',axis = 1)
    # Removendo as linhas que  estão com pelo menos com um valor vázio
tabela_clientes = tabela_clientes.dropna(how = 'any',axis = 0)


# In[6]:


# Base de dados após os tratamentos, percebemos que temos uma base de dados limpa e pronta para as próximas etapas
display(tabela_clientes.info())
display(tabela_clientes.isna().sum())


# In[7]:


# Passo 4: identificar como estão destribuídos os churns/cancelamentos
display(tabela_clientes['Churn'].value_counts())
    # Visualização em formato de percentual: dessa forma foi identificado o percentual dos clientes que cancelaram
display(tabela_clientes['Churn'].value_counts(normalize = True).map('{:.2%}'.format))


# In[8]:


# Passo 5: identificar as causas raiz dos cancelamentos
import plotly.express as px


# In[9]:


for coluna in tabela_clientes:
    grafico = px.histogram(tabela_clientes, x = coluna, color = tabela_clientes['Churn'] )
    grafico.show()


# ### Conclusões e Ações

# Escreva aqui suas conclusões:
# 
# - Maior concentração dos churns estão nos primeiros meses
#     - 
# - Fibra é o serviço com maior concentração dos churns
#     -
# - Clientes com mais serviços tendem a não cancelar
#     -
# - Serviços na modalidade de contrato mensal tendem a ser cancelados
#     -
# - Serviços pagos no boleto tendem a ser cancelados
#     -
# - Clientes sem o serviço de suporte ao cliente tendem a cancelar
#     -
# - Clientes sem o serviço de proteção ao equipamento tendem a cancelar
#     -
# - Clientes sem o serviço de backup online tendem a cancelar
#     -
# - Clientes sem o serviço de segurança online tendem a cancelar
#     -
# 
# --- Essas duas ações direcionadas especificamente aos clientes que contrataram o serviço de Fibra Ótica
# ---
# --- Com os esses pontos pode-se inferir que os primeiros meses são cruciais para a permanencia ou não do cliente; Uma boa abordagem e a qualificação da venda com uma forte atuação no pós-venda para mantermos uma proximação com o cliente para sanarmos suas principais dificuldades com o serviço nos primeiros meses; Para isso uma ação na qualificação da venda, a oferta do serviço de suporte ao cliente, sempre que o cliente precisar nas suas demandas personalizadas possa ser atendido de forma rápida e eficiente; Outra ação de qualificação de venda, incentivar as formas de pagamento débito automático ou cartão de crédito, dessa forma o cliente não precisa se preocupar com o pagamento das faturas, sendo que as faturas serão pagas de forma automática.
# ---
# --- Com essas duas ações já será possível sanar duas grandes dores dos clientes, nesse primeiro momento as dúvidas sobre o serviço contrato, suporte nas dificuldades técnicas e despreocupação com o pagamento das faturas.
# --- 
# --- Uma terceira ação que pode-se ser tomada, oferta de serviços adicionais que façam sentido para o cliente e que ele veja como soluções. Uma estratégia de oferta de serviços adicionais, a personalização conforme a realidade de cada cliente. Isso para que não seja oferta um sequência de serviços que não façam menor sentido para ele.
# ---
# 
