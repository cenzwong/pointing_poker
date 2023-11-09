import streamlit as st
import sqlite3
import pandas as pd

conn_sqlite = sqlite3.connect('test.sqlite')
cur_sqlite = conn_sqlite.cursor()

cur_sqlite.execute('create table if not exists test (1 int, b int)')
conn_sqlite.commit()

st.write('Hello habagya!')
