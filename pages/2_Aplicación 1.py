import streamlit as st
import time

hora_actual = time.strftime("%H:%M:%S")
st.write("La hora actual es:", hora_actual)