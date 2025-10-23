import streamlit as st
import streamlit.components.v1 as components

st.title("Print Demo")

st.write("Click the button below to print this page.")

# Create a native Streamlit button that triggers print
if st.button("Print", type="primary"):
    # Inject JavaScript to trigger print dialog
    # This uses a proper Streamlit component which ensures the print
    # is triggered from a trusted user interaction context
    # The script executes immediately and the iframe can be removed after
    components.html(
        """
        <script>
            window.print();
            // Remove the iframe after print dialog is triggered
            setTimeout(function() {
                var iframe = window.frameElement;
                if (iframe && iframe.parentNode) {
                    iframe.parentNode.removeChild(iframe);
                }
            }, 100);
        </script>
        """,
        height=0,
    )
