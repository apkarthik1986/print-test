import streamlit as st
import streamlit.components.v1 as components

st.title("Print Demo")

st.write("Click the button below to print this page.")

# Create a native Streamlit button that triggers print
if st.button("Print"):
    # Use session state to create a unique key for each print action
    # (SessionState doesn't implement setdefault reliably in all Streamlit versions,
    # so use get/assignment which is compatible.)
    st.session_state["print_count"] = st.session_state.get("print_count", 0) + 1

    # Inject JavaScript to trigger print dialog.
    # Use a small positive height (0 can cause errors in some Streamlit versions).
    # Use onload to ensure print runs after the iframe loads.
    html = """
    <html>
      <body onload="window.print()">
        <script>/* printing frame */</script>
      </body>
    </html>
    """
    components.html(html, height=1, key=f"print_{st.session_state['print_count']}")
