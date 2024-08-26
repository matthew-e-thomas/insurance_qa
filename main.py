import streamlit as st
from pypdf import PdfReader

st.title("Insurance Q & A")
uploaded_policy = st.file_uploader("Your Insurance Policy", type=['pdf'])
policy = PdfReader(uploaded_policy)
page = policy.pages
policy_text = page.extract_text()