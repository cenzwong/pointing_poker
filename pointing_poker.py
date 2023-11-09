import streamlit as st
import sqlite3
import pandas as pd

conn_sqlite = sqlite3.connect('test.sqlite')
cur_sqlite = conn_sqlite.cursor()

cur_sqlite.execute('create table if not exists test (1 int, b int)')
conn_sqlite.commit()

tt = pd.read_sql_query('select a from test', conn_sqlite)['a'].to_list()

if len(tt) = 0 :
  cur_sqlite.execute("""insert into test values ('1', '1')""")


st.write('Hello habagya!')
