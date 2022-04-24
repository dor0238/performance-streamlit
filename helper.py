import sqlite3
import streamlit as st
import pandas as pd
import sqlalchemy


def getAllData(sqlString,path):
    db = sqlite3.connect(path)
    cur = db.cursor(sqlString)
    cur.execute(sqlString)
    return cur.fetchall()

def crud(sqlString, path):
    db = sqlite3.connect('Performance.db')
    c = db.cursor()
    c.execute(sqlString)
    db.commit()
    db.close()

def lightspeed():
    st.title('Light Speed Project Results')
    con = sqlite3.connect('Performance.db')
    df = pd.read_sql_query('SELECT * from Results', con)
    st.write(df)




