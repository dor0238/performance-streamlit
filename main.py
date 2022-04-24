from helper import *
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import sqlalchemy

with st.sidebar:
    selected = option_menu(
        menu_title='Menu',
        options=['Home', 'Projects','Login','Signup'],
        default_index=0,


    )


if selected == 'Home':
    st.title('Performance DB')
    st.header('Insert Results Here:')


    tests = (
        'Maximum connections rate',
        'Max concurrent connections',
        'CPent- FW only VLAN bidirectional SNIC',
        'CPent- FW only VLAN bidirectional SNIC + 10G bond * 2',
        'Cpent- FW + IPS',
        'Cpent- NGFW',
        'Cpent- NGTP',
        'CPent- FW only VLAN bidirectional Low Latency mode',
        'Maximum connections rate, 1k response, 2k cert, NGFW',
        'SSL CPent- NGFW 2K',
        'SSL CPent - NGTP 2K',

    )

    enter_name = st.selectbox('Enter Name', ('Dor Elia', 'Irina Kitaev'))
    select_test = st.selectbox('Select Tests', tests)
    select_machine = st.selectbox('Select Machine', ('QLS250', 'QLS450', 'QLS650', 'QLS800'))
    select_Snic_total = st.selectbox('How many SNIC?', (1, 2, 3, 4))
    select_policy = st.selectbox('Select Policy', ('Standard_CPEnt', 'Standard_CPS'))
    enter_result = st.number_input('Enter Result', min_value=0)


    if st.button('Submit Result'):
        insertSQL = f"""
            INSERT INTO Results(Name,Test,Machine,SmartNics,Policy,Result,Comment)
                VALUES (
                '{enter_name}',
                '{select_test}',
                '{select_machine}',
                '{select_Snic_total}',
                '{select_policy}',
                '{enter_result}';
            """
        crud(insertSQL, 'Performance.db')

if selected == 'Login':
    st.subheader('Please Login')

    username = st.text_input('User Name')
    password = st.text_input('Password',type='password')
    if st.button("Login"):
        st.success("Logged In as {}".format(username))
        task = st.selectbox("Task",["Insert Result"])
        if task == "Insert Result":
            st.button('Submit Result')



if selected == 'Signup':
    st.subheader("Create New Account")


if selected == 'Projects':


    con = sqlite3.connect('Performance.db')
    c = con.cursor()

    c.execute('''
              SELECT
              *
              FROM Results
              ''')
    machines_option = ('Select Machine', ('QLS250', 'QLS450', 'QLS650', 'QLS800'))
    df = pd.DataFrame(c.fetchall(), columns=['Name', 'Test', 'Machine','SmartNics','Policy','Result'])
        #sidbar#
    st.sidebar.header('Please Filter Here:')
    machine = st.sidebar.multiselect(
        'Select Machine:',
        options=df["Machine"].unique(),


    )
    test = st.sidebar.multiselect(
        'Select Test:',
        options=df["Test"].unique(),


    )
    name = st.sidebar.multiselect(
        'Select Name:',
        options=df["Name"].unique(),


    )
    nics = st.sidebar.multiselect(
        'Select SmartNIC:',
        options=df["SmartNics"].unique(),


    )

    df_selection = df.query(
        "Name == @name | Test == @test | Machine == @machine | SmartNics == @nics  "
    )

    st.dataframe(df_selection,1000,1000)












