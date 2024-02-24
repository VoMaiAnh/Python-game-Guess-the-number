# -*- coding: utf-8 -*-
"""
Created on Sun Feb 2024

@author: Mai Anh Võ
"""

import numpy as np
import pickle
import streamlit as st
import getpass
import random
import pandas as pd
import matplotlib.pyplot as plt 

rondas = {'Modo':[], 'Nivel':[], "Intentos":[], 'Punto':[]}

def facil(respuesta):
    for i in range(20):
        num = int(st.text_input("Adivina el número: "))
        if num == respuesta:
            st.success("¡Enhorabuena! ¡Has ganado!")
            rondas['Punto'].append(1)
            break
        elif (num > respuesta) and (i<18):
            st.write("Es MAYOR que la respuesta correcta. Te quedan " + f"{19-i}" 
                  + " intentos. Inténtalo de nuevo!")
        elif (num < respuesta) and (i<18):
            st.write("Es MENOR que la respuesta correcta. Te quedan " + f"{19-i}"
                  + " intentos. Inténtalo de nuevo!")
        elif (num > respuesta) and (i==18):
            st.write("Es MAYOR que la respuesta correcta. Último intento. ¡Ánimo!")
        elif (num < respuesta) and (i==18):
            st.write("Es MENOR que la respuesta correcta. Último intento. ¡Ánimo!")
    if num != respuesta:
        st.error("¡Has perdido!")
        rondas['Punto'].append(0)
    rondas['Intentos'].append(i+1)

def medio(respuesta):
    for i in range(12):
        num = int(st.text_input("Adivina el número: "))
        if num == respuesta:
            st.success("¡Enhorabuena! ¡Has ganado!")
            rondas['Punto'].append(1)
            break
        elif (num > respuesta) and (i<10):
            st.write("Es MAYOR que la respuesta correcta. Te quedan " + f"{11-i}" 
                  + " intentos. Inténtalo de nuevo!")
        elif (num < respuesta) and (i<10):
            st.write("Es MENOR que la respuesta correcta. Te quedan " + f"{11-i}"
                  + " intentos. Inténtalo de nuevo!")
        elif (num > respuesta) and (i==10):
            st.write("Es MAYOR que la respuesta correcta. Último intento. ¡Ánimo!")
        elif (num < respuesta) and (i==10):
            st.write("Es MENOR que la respuesta correcta. Último intento. ¡Ánimo!")
    if num != respuesta:
        st.error("¡Has perdido!")
        rondas['Punto'].append(0)
    rondas['Intentos'].append(i+1)

def dificil(respuesta):
    for i in range(5):
        num = int(st.text_input("Adivina el número: "))
        if num == respuesta:
            st.success("¡Enhorabuena! ¡Has ganado!")
            rondas['Punto'].append(1)
            break
        elif (num > respuesta) and (i<3):
            st.write("Es MAYOR que la respuesta correcta. Te quedan " + f"{4-i}" 
                  + " intentos. Inténtalo de nuevo!")
        elif (num < respuesta) and (i<3):
            st.write("Es MENOR que la respuesta correcta. Te quedan " + f"{4-i}"
                  + " intentos. Inténtalo de nuevo!")
        elif (num > respuesta) and (i==3):
            st.write("Es MAYOR que la respuesta correcta. Último intento. ¡Ánimo!")
        elif (num < respuesta) and (i==3):
            st.write("Es MENOR que la respuesta correcta. Último intento. ¡Ánimo!")
    if num != respuesta:
        st.error("¡Has perdido!")
        rondas['Punto'].append(0)
    rondas['Intentos'].append(i+1)



def main():
    st.title("Guess the Number")

    modo = st.sidebar.radio("Selecciona el modo:", ["Partida modo solitario", "Partida 2 jugadores", "Estadística", "Salir"])
    nivel = st.sidebar.radio("Elige tu nivel:", ["Fácil (20 intentos)", "Medio (12 intentos) ", "Difícil (5 intentos)"])

    if modo == "Partida modo solitario":
        rondas['Modo'].append('Solo')
        respuesta = random.randint(1, 1000) # Genera un número aleatorio
        if nivel == "Fácil (20 intentos)":
            rondas['Nivel'].append('Fácil')
            facil(respuesta)
        elif nivel == "Medio (12 intentos)":
            rondas['Nivel'].append('Medio')
            medio(respuesta)
        elif nivel == "Difícil (5 intentos)":
            rondas['Nivel'].append('Difícil')
            dificil(respuesta)
    elif modo == "Partida 2 jugadores": 
        rondas['Modo'].append('Duo')
        respuesta = int(getpass.getpass('Introduzca un número entre 1 y 1000: '))
        if nivel == "Fácil (20 intentos)":
            rondas['Nivel'].append('Fácil')
            facil(respuesta)
        elif nivel == "Medio (12 intentos)":
            rondas['Nivel'].append('Medio')
            medio(respuesta)
        elif nivel == "Difícil (5 intentos)":
            rondas['Nivel'].append('Difícil')
            dificil(respuesta)
    elif modo == "Estadística":
        resumen = pd.DataFrame.from_dict(rondas)
        st.write(resumen)
        st.write(f"Has ganado {resumen['Punto'].sum()} de {resumen['Punto'].count()} partidas!")


if __name__ == "__main__":
    main()
