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

def facil():
    for i in range(20):
        num = int(st.text_input("Adivina el número: "))
        if num == respuesta:
            print("Enhorabuena!!! Has ganado.")
            rondas['Punto'].append(1)
            break
        elif (num > respuesta) & (i<18):
            print("Es MAYOR que la respuesta correcta. Te quedan " + f"{19-i}" 
                  + " intentos. Inténtalo de nuevo!")
        elif (num < respuesta) & (i<18):
            print("Es MENOR que la respuesta correcta. Te quedan " + f"{19-i}"
                  + " intentos. Inténtalo de nuevo!")
        elif (num > respuesta) & (i==18):
            print("Es MAYOR que la respuesta correcta. Último intento. Ánimo!!!")
        elif (num < respuesta) & (i==18):
            print("Es MENOR que la respuesta correcta. Último intento. Ánimo!!!")
    if num != respuesta:
        print("Has perdido")
        rondas['Punto'].append(0)
    rondas['Intentos'].append(i+1)

def medio():
    for i in range(12):
        num = int(st.text_input("Adivina el número: "))
        if num == respuesta:
            print("Enhorabuena!!! Has ganado.")
            rondas['Punto'].append(1)
            break
        elif (num > respuesta) & (i<10):
            print("Es MAYOR que la respuesta correcta. Te quedan " + f"{11-i}" 
                  + " intentos. Inténtalo de nuevo!")
        elif (num < respuesta) & (i<10):
            print("Es MENOR que la respuesta correcta. Te quedan " + f"{11-i}"
                  + " intentos. Inténtalo de nuevo!")
        elif (num > respuesta) & (i==10):
            print("Es MAYOR que la respuesta correcta. Último intento. Ánimo!!!")
        elif (num < respuesta) & (i==10):
            print("Es MENOR que la respuesta correcta. Último intento. Ánimo!!!")
    if num != respuesta:
        print("Has perdido")
        rondas['Punto'].append(0)
    rondas['Intentos'].append(i+1)

def dificil():
    for i in range(5):
        num = int(st.text_input("Adivina el número: "))
        if num == respuesta:
            print("Enhorabuena!!! Has ganado.")
            rondas['Punto'].append(1)
            break
        elif (num > respuesta) & (i<3):
            print("Es MAYOR que la respuesta correcta. Te quedan " + f"{4-i}" 
                  + " intentos. Inténtalo de nuevo!")
        elif (num < respuesta) & (i<3):
            print("Es MENOR que la respuesta correcta. Te quedan " + f"{4-i}"
                  + " intentos. Inténtalo de nuevo!")
        elif (num > respuesta) & (i==3):
            print("Es MAYOR que la respuesta correcta. Último intento. Ánimo!!!")
        elif (num < respuesta) & (i==3):
            print("Es MENOR que la respuesta correcta. Último intento. Ánimo!!!")
    if num != respuesta:
        print("Has perdido")
        rondas['Punto'].append(0)
    rondas['Intentos'].append(i+1)



def main():
    st.title("Guess the Number")

    modo = st.sidebar.radio("Selecciona el modo:", ["Partida modo solitario", "Partida 2 jugadores", "Estadística", "Salir"])
    nivel = st.sidebar.radio("Elige tu nivel:", ["Fácil (20 intentos)", "Medio (12 intentos) ", "Difícil (5 intentos)"])

    if modo == "1":
        rondas['Modo'].append('Solo')
        respuesta = random.randint(1, 1000) # Genera un número aleatorio
        if nivel == "1":
            rondas['Nivel'].append('Fácil')
            facil()
        elif nivel == "2":
            rondas['Nivel'].append('Medio')
            medio()
        elif nivel == "3":
            rondas['Nivel'].append('Difícil')
            dificil()
    elif modo == "2": 
        rondas['Modo'].append('Duo')
        respuesta = int(getpass.getpass('Introduzca un número entre 1 y 1000: '))
        if nivel == "1":
            rondas['Nivel'].append('Fácil')
            facil()
        elif nivel == "2":
            rondas['Nivel'].append('Medio')
            medio()
        elif nivel == "3":
            rondas['Nivel'].append('Difícil')
            dificil()
    elif modo == "3":
        resumen = pd.DataFrame.from_dict(rondas)
        print(resumen)
        print("Has ganado " + f"{resumen['Punto'].sum()}" +" de " + f"{resumen['Punto'].count()}"+" partidas!")


if __name__ == "__main__":
    main()
