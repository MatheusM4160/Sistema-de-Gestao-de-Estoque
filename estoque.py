import sqlite3
import pandas as pd
import streamlit as st

conn = sqlite3.connect('register.db')

query = 'SELECT * FROM estoque'

df = pd.read_sql_query(query, conn)

st.title('Estoque')
st.dataframe(df)