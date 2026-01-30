import numpy as np
import streamlit as st

st.header("Calculate your basics here!")

expression = st.text_input("Expression: ")

col1, col2, col3, col4 = st.columns(4)


with col1:
    one = st.button("1", use_container_width=True)
    two = st.button("4", use_container_width=True)
    three = st.button("7", use_container_width=True)
    backspace = st.button("Backspace", use_container_width=True)

with col2:
    four = st.button("2", use_container_width=True)
    five = st.button("5", use_container_width=True)
    six = st.button("8", use_container_width=True)
    zero = st.button("0", use_container_width=True)


with col3:
    seven = st.button("3", use_container_width=True)
    eight = st.button("6", use_container_width=True)
    nine = st.button("9", use_container_width=True)
    clear = st.button("Clear", use_container_width=True)

with col4:
    add = st.button("Add", use_container_width=True)
    sub = st.button("Subtract", use_container_width=True)
    mul = st.button("Multiply", use_container_width=True)
    div = st.button("Divide", use_container_width=True)

