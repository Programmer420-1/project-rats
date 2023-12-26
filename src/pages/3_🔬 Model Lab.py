import streamlit as st
import asyncio
import json

from util.connector import make_inference, get_inference_status
import streamlit as st
from PIL import Image

from widgets.general import normal_text, vertical_gap, subtitle
from util.custom_theme import load_css, load_modellab_css
import params

import os

# Set page configuration for better aesthetics
st.set_page_config(
    page_title="Project RATS | Model Lab",
    layout="wide",
    page_icon= Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'favicons', 'favicon-16x16.png'))
)

# Function to main app
def main():
    # custom styling
    load_css()
    load_modellab_css()

    # session initialization
    initialize_session_state()

    # Set the title of the app
    st.header("Welcome to Model Lab 🔬")
    st.markdown("""
        <div class='subtitle-container'>
            <span class='h6 subtitle'>Discover the capabilities of <span class='project-rats'><span class='project'>Project&nbsp&nbsp</span><span class='rats'>RATS</span></span> at your fingertips. 🚀 Dive into a world of different models and see how they stack up with easy comparisons. 🔍 Explore, analyze, and unleash the potential with just a few clicks! 🧪✨</span>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Step 1: Pick a model")
    st.markdown("""
        <div class='subtitle-container'>
            <span class='h6 subtitle'>Select a preferred model from the list</span>
        </div>
    """, unsafe_allow_html=True)

    # Dropdown selector
    model_choice = st.selectbox(
    '',
    params.MODEL_CHOICE, label_visibility='hidden')

    vertical_gap(2)    
    st.subheader("Step 2: Upload and Infer Abdominal CT Study")
    st.markdown("""
        <div class='subtitle-container'>
            <span class='h6 subtitle'>Upload a <code>.zip</code> file containing the CT images series. Currently, only CT images series in DICOM (<code>.dcm</code>) format is supported. Click <code>Process File</code> button to start the inference.</span>
        </div>
    """, unsafe_allow_html=True)


    # File uploader widget
    uploaded_file = st.file_uploader("", label_visibility='hidden', type="zip")

    output_container = st.container()
    dynamic_content = output_container.empty()

    if uploaded_file is not None:
        if st.session_state['current_task_id'] is None:
#           # Create a button that appears after file is uploaded
            if dynamic_content.button("Process File"):
                # when pressed, the file is uploaded and current_task_id is saved to session
                upload(uploaded_file, model_choice, dynamic_content)
        
    
    if st.session_state['process_result'] is not None:
        vertical_gap(2)
        output_container.json(st.session_state['process_result'])

    if not st.session_state['is_processing'] and st.session_state['status_logging'][-1] == '<ENDOFPROCESS>':
        vertical_gap(2)
        if output_container.button("Process Next"):
            initialize_session_state()
            st.rerun()


def upload(uploaded_file, model_choice, container, patient_id="0", series_id="0"):
    # get task ID
    result = asyncio.run(make_inference(uploaded_file, patient_id, series_id, model_choice))
    st.session_state['current_task_id'] = result['task_id']
    st.session_state['is_processing'] = True

    asyncio.run(update_status(result['task_id'], container))
    # st.rerun()

def initialize_session_state():
    st.session_state['process_result'] = None
    st.session_state['current_task_id'] = None
    st.session_state['status_logging'] = ["▶️ Initializing request..."]
    st.session_state['is_processing'] = False

async def update_status(task_id, container):
    # Create a placeholder for dynamic content within the container
    container.empty()
    container.markdown(f"""
                <span class='h5'>Inference Server Status</span>
                <div class='output-container'>
                    {''.join(f'<span class="h6">{log}</span>' for log in st.session_state["status_logging"] if "model" not in log)}
                </div>
            """, unsafe_allow_html=True)
    while True:
        status = await get_inference_status(task_id)
        if status:
            status_messages = status['status']

            # Append new messages to the session state list
            for message in status_messages:
                if message not in st.session_state["status_logging"]:
                    st.session_state["status_logging"].append(message)

            # Update the dynamic content
            container.markdown(f"""
                <span class='h5'>Inference Server Status</span>
                <div class='output-container'>
                    {''.join(f'<span class="h6">{log}</span>' for log in st.session_state["status_logging"] if "model" not in log)}
                </div>
            """, unsafe_allow_html=True)

            if "<ENDOFPROCESS>" in status_messages:
                st.session_state['process_result'] = st.session_state["status_logging"][-2]
                st.session_state['is_processing'] = False
                break

            await asyncio.sleep(0.5)  # Non-blocking wait
        else:
            st.session_state["status_logging"].append("[FATAL] Failed to get task status.")
            container.text('\n'.join(st.session_state["status_logging"]))
            break

main()