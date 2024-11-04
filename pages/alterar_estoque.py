import streamlit as st
import sqlite3

def Pesquisar(Product):
    with sqlite3.connect('resgister.db') as conn:
        cursor = conn.cursor()

        #continuar a escrever a logica de pesquisa, vou parar por hj

st.title('Alterar Estoque')

st.text_input(label='Pesquisar', placeholder='Ex.: Tecido', label_visibility='collapsed')

st.button(label='Pesquisar', on_click=lambda: Pesquisar())