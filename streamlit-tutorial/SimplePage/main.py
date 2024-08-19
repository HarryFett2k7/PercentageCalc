import streamlit as st
from PIL import Image

st.header("Percentage calculator", divider="rainbow" )
st.subheader("A simple tool to calculate percentage change.")

st.markdown('''
    This is a test while the website is under development
''')

increase = st.toggle("Increase")
decrease = st.toggle("Decrease")

if increase:
    start_entered = st.number_input("Enter start number: ", value = 0.01)
    final_entered = st.number_input("Enter final number: ", value = 0.01)
    def calc(pStart, pFinal):
        return (pFinal - pStart) / pStart * 100
    output = calc(start_entered, final_entered)
    st.markdown("+" + str(output) + "%")
    

if decrease:
    start_entered1 = st.number_input("Enter start number: ", value = 0.01)
    final_entered1 = st.number_input("Enter final number: ", value = 0.01)
    def calc(pStart, pFinal):
        return (pStart - pFinal) / pStart * 100
    output1 = calc(start_entered1, final_entered1)
    st.markdown("-" + str(output1) + "%")
