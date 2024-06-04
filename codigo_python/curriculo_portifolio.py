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

def inform_geral():
    
    #### RESUMO GERAL
    st.subheader('Resumo')
    
    with st.container(border = True):
        st.text(
            
            '''
            Sou Bacharel em Estatística e Mestre em Economia pela Universidade Federal do
            Ceará (UFC). Tenho experiência em análise de dados: análise descritiva de 
            dados (elaboração de gráficos e tabelas, dashboards), análise estatística 
            inferencial (testes de hipóteses, estimação de modelos estatísticos), construção 
            de modelos estatísticos e machine learning para previsão (modelos de regressão 
            linear e logística, modelos de séries temporais). Tenho bons conhecimentos em 
            linguagem de programação (Python, R, Git/GitHub).
            '''
            
            )

    st.divider()
    #### FIM RESUMO GERAL
    
    #### FORMAÇÃO ACADEMICA
    st.subheader('Formação Acadêmica')
    with st.container(border = True):
        st.markdown(
            
            '''
            * Bachalelado em Estatítica: Universidade Federal do Ceará
            * Mestrado em Economia: Universidade Federal do Ceará
            '''
            
            )
        
    st.divider()
    #### FIM FORMAÇÃO ACADEMICA
    
    #### CURSOS DE APERFEIÇOAMENTO
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
    
    #### FIM CURSOS DE APERFEIÇOAMENTO
    
def exp_prof():
    
    #### SESA
    st.markdown(
        '''
        ### Secretaria da Saúde do Estado do Ceará (SESA)
        #### Analista de Gestão (Dados)
        jul/2023-atual
        '''
        )
    
    with st.container(border = True):
        st.markdown(
            '''
            **Atividades realizadas:**
            * reunir informações de várias fontes, como registros médicos, dados de pacientes, pesquisas e estudos clínicos;
            * limpar e organizar os dados, garantindo que estejam prontos para análise;
            * utilizar técnicas estatísticas/econométricas/ML, para explorar os dados identificando padrões, tendências e correlações epidemiológicas;
            * traduzir os resultados da análise em gráficos e tabelas;
            * desenvolver modelos preditivos que auxiliem na previsão de demandas assistenciais.
            
            **Ferramentas utilizadas:** Excel, Google sheet, Software R, python, Power BI
            '''
            )
    st.divider()
    ####
    
    #### Cearáprev
    st.markdown(
        '''
        ### Cearáprev
        #### Analista de Dados
        jan/2022-abr/2023
        '''
        )
    with st.container(border = True):
        st.markdown(
            '''
            **Atividades realizadas:**
            * Construção de base de dados para acompanhamento de desempenho e produtividade;
            
            **Ferramentas utilizadas:** Excel, Google sheet, Software R
            '''
            )
    st.divider()
    ####
    
    #### UFC - Professor
    st.markdown(
        '''
        ### Universidade Federal do Ceará
        #### Professor Substituto
        ago/2019-maio/2021
        '''
        )
    with st.container(border = True):
        st.markdown(
            '''
            **Disciplinas ministradas:**
            * Probabilidade e Estatística;
            * Análise de Regressão;
            * Análise de Séries Temporais;
            * Processos Estocasticos.
            
            
            **Ferramentas utilizadas:** Software R
            '''
            )
    st.divider()
    ####
    
    #### LECO-CAEN/UFC
    st.markdown(
        '''
        ### Laboratório de Econometria e Otimização - CAEN/UFC
        #### Estatístico (contrato de prestação de serviços)
        jan/2019-jan/2020
        '''
        )
    with st.container(border = True):
        st.markdown(
            '''
            **Atividades realizadas:**
            * Elaboração de questionários, via plataforma CAPI Survey Solution; 
            * Limpeza e pocessamento de bases de dados;
            * Análise descritiva e inferencial de dados;
            * Construção de modelos de regressão/machine learning.
            
            **Ferramentas utilizadas:** Excel, Software R, CAPI Survey Solution
            '''
            )

tab1, tab2, tab3 = st.tabs(['Resumo Geral', 'Experiência Proficional', 'Portifólio'])

with tab1:
    inform_geral()
with tab2:
    exp_prof()