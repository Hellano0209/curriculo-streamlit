#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:43:22 2024

@author: hellano
"""

import streamlit as st

# SIDEBAR
# dados para contato
st.sidebar.link_button('Linkedin', 'https://www.linkedin.com/in/hellano-vieira-de-almeida-b4987359/') 
st.sidebar.write('e-mail: hellano.vda@gmail.com')
st.sidebar.write('telefone: (85) 99688-6866')

st.header('Hellano Vieira de Almeida', divider=True)

st.subheader('Resumo')
with st.container(border = True):
    st.text(
        
        '''
        Sou Bacharel em Estatística e Mestre em Economia pela Universidade Federal do
        Ceará (UFC). Tenho experiência em análise de dados como: análise descritiva de 
        dados (elaboração de gráficos e tabelas, dashboards), análise estatística 
        inferencial (testes de hipóteses, estimação de modelos estatísticos), construção 
        de modelos estatísticos e machine learning para previsão (modelos de regressão 
        linear e logística, modelos de séries temporais). Tenho bons conhecimentos em 
        linguagem de programação (Python, R, Git/GitHub).
        '''
        
        )

st.divider()
    
st.subheader('Formação Acadêmica')
with st.container(border = True):
    st.markdown(
        
        '''
        * Bachalelado em Estatítica: Universidade Federal do Ceará
        * Mestrado em Economia: Universidade Federal do Ceará
        '''
        
        )
    
st.divider()

st.subheader('Cursos de Aperfeiçoamento')
with st.container(border = True):
    st.markdown(
        '''
        * Fundamentos de Linguagem Python para Análise de Dados e Data Science - Nível Intermediário
        * Microsoft Power BI Para Business Intelligence e Data Science
        * Análise de Viabilidade Econômica e Financeira de Projetos
        * Versionamento de Código com Git e GitHub
        '''
        
        )