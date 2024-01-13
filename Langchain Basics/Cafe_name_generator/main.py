import streamlit as st
import langchain_helper

st.title("Cafe Name generator")

cuisine = st.sidebar.selectbox('Pick a Cuisine', ('Indian', 'Italian', 'Mexican', 'Arabic', 'American', 'Chinese', 'European'))


if cuisine:
    response = langchain_helper.generate_cafe_name_items(cuisine)
    st.header(response['cafe_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write('**Menu Items**')
    for item in menu_items:
        st.write('-',item)
