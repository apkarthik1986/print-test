import streamlit as st
import streamlit.components.v1 as components

st.title("Print Demo")

st.write("Click the button below to print this page.")

# Create a native Streamlit button that triggers print
if st.button("Print", type="primary"):
    # Inject JavaScript to trigger print dialog
    # This uses a proper Streamlit component which ensures the print
    # is triggered from a trusted user interaction context
    components.html(
        """
        <script>
            window.print();
        </script>
        """,
        height=0,
    )
