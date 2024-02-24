# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 00:44:14 2024

@author: admin
"""
import streamlit as st

modo = st.sidebar.radio("Selecciona el modo:", ["Partida modo solitario", "Partida 2 jugadores", "Estadística", "Salir"])
nivel = st.sidebar.radio("Elige tu nivel:", ["Fácil (20 intentos)", "Medio (12 intentos) ", "Difícil (5 intentos)"])

