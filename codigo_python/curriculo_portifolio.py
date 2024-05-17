#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:43:22 2024

@author: hellano
"""

import streamlit as st
from PIL import Image

st.header('Hellano Vieira de Almeida')

# Open the image from the specified path
image = Image.open('~/Documentos/Projetos Python/Currículo e Portifólio/curriculo-streamlit/imagens/foto_perfil.jpg')
st.image(image)