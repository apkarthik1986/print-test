import streamlit as st
import streamlit.components.v1 as components

st.title("Print Demo")
st.write("Click the button below to print this page.")

if st.button("Print"):
    # Inject a tiny HTML snippet that triggers the browser print dialog.
    components.html('<script>window.print()</script>', height=1)
