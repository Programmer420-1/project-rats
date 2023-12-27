import streamlit as st
import streamlit.components.v1 as components

import params

def load_css():
    with open(params.GLOBAL_CSS, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def load_overview_css():
    with open(params.OVERVIEW_CSS, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def load_modellab_css():
    with open(params.MODEL_LAB_CSS, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def is_dark_theme():
    """Check if the user prefers a dark theme."""
    # JavaScript to check the system preference
    js = """
    <script>
    var isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    // Streamlit uses "streamlit:componentReady" event to trigger data back to Python
    window.parent.postMessage({
      isDarkTheme: isDark,
      type: 'streamlit:setComponentValue',
    }, '*');
    </script>
    """
    # Render the JavaScript in a Streamlit component
    components.html(js, height=0)  # Height 0 to make it invisible

    # Listen for the response from JavaScript
    return st.session_state.get('isDarkTheme', False)

