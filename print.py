import streamlit as st

st.title("Print Demo")

st.write("Click the button below to print this page.")

# Inject JavaScript for print functionality
print_js = """
    <script>
    function printPage(){
        window.print();
    }
    </script>
    <button onclick="printPage()">Print</button>
"""

st.markdown(print_js, unsafe_allow_html=True)
