import streamlit as st
import sqlite3
import pandas as pd

conn_sqlite = sqlite3.connect('test.sqlite')
cur_sqlite = conn_sqlite.cursor()

cur_sqlite.execute('create table if not exists test (a int, b int)')
conn_sqlite.commit()

tt = pd.read_sql_query('select * from test', conn_sqlite)
ttt = tt['a'].to_list()

if len(tt) == 0 :
  cur_sqlite.execute("""insert into test values ('1', '1')""")
  conn_sqlite.commit()


st.write('Hello habagya!')
st.write(tt)
