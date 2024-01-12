import streamlit as st
import asyncio
import json
import pandas as pd

from util.connector import make_inference, get_inference_status
import streamlit as st
from PIL import Image

from widgets.general import normal_text, vertical_gap, subtitle
from util.custom_theme import load_css, load_modellab_css
from widgets.eda import load_csv
import params

import os

# Set page configuration for better aesthetics
st.set_page_config(
    page_title="Project RATS | Model Lab",
    layout="wide",
    page_icon= Image.open(os.path.join('static', 'favicons', 'favicon-16x16.png'))
)

# Function to main app
def main():
    # custom styling
    load_css()
    load_modellab_css()

    # session initialization
    initialize_session_state()

    if params.DEBUG:
        mock_result = {
            "model" : "default",
            "result": {
                "n_imgs" : 100,
                "elapse_time": 26.080299854278564,
                "inference": {
                    "patient_id": "0",
                    "bowel_healthy" : 0.9715576171875,
                    "bowel_injury" : 0.0284423828125,
                    "extravasation_healthy" :0.8140869140625,
                    "extravasation_injury" : 0.1859130859375,
                    "kidney_healthy" : 0.8896484375,
                    "kidney_low": 0.06646728515625,
                    "kidney_high" : 0.0438232421875,
                    "liver_healthy" : 0.9638671875,
                    "liver_low" : 0.03179931640625,
                    "liver_high" : 0.004482269287109375,
                    "spleen_healthy" : 0.95703125,
                    "spleen_low" : 0.03619384765625,
                    "spleen_high" : 0.006992340087890625 
                }
            }
       }
        st.session_state['process_result'] = mock_result

    # Set the title of the app
    st.header("Welcome to Model Lab 🔬")
    st.markdown("""
        <div class='subtitle-container'>
            <span class='h6 subtitle'>Discover the capabilities of <span class='project-rats'><span class='project'>Project&nbsp&nbsp</span><span class='rats'>RATS</span></span> at your fingertips. 🚀 Dive into a world of different models and see how they stack up with easy comparisons. 🔍 Explore, analyze, and unleash the potential with just a few clicks! 🧪✨</span>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.info("This is a demonstration version. Ground truth labels will be provided for comparisons whenever possible.")
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
                try:
                    st.session_state['patient_id'] = uploaded_file.name.split("_")[0]
                    st.session_state['series_id'] = uploaded_file.name.split("_")[1][:-4]
                except Exception as e:
                    st.session_state['patient_id'] = "0"
                    st.session_state['series_id'] = "0"
                    st.toast("Patient ID or Series ID not provided", icon="❗")
                upload(uploaded_file, model_choice, dynamic_content)
        
    
    if st.session_state['process_result'] is not None:
        vertical_gap(2)
        n_imgs = st.session_state['process_result']['result']['n_imgs']
        elapse_time = st.session_state['process_result']['result']['elapsed_time']
        patient_id = st.session_state['patient_id']
        series_id = st.session_state['series_id']
        inference_result = st.session_state['process_result']['result']['inference']
        
        del inference_result['patient_id']

        # Split the dictionary into two based on label type
        binary_data = {}
        triple_data = {}

        for key, value in inference_result.items():
            organ, label = key.rsplit('_', 1)
            if organ in ['bowel', 'extravasation']:
                binary_data.setdefault(organ, []).append(value)
            else:
                triple_data.setdefault(organ, []).append(value)


        # Create the DataFrames
        binary_df = pd.DataFrame(binary_data, index=['healthy', 'injured']).T
        triple_df = pd.DataFrame(triple_data, index=['healthy', 'injured_low', 'injured_high']).T

        # Results
        output_container.markdown("<span class=h5>Results</span>", unsafe_allow_html=True)
        output_container.markdown(f"""
            Number of Image Processed: {n_imgs}  
            Elapsed Time: {elapse_time:.2f} seconds  
            Patient_ID: {"Not provided" if patient_id == "0" else patient_id}  
            Series_ID: {"Not provided" if series_id == "0" else series_id}
        """)

        # Processing result
        # Process binary_df to get the highest confidence
        binary_df_ = binary_df.copy()
        binary_df_[['Predicted', 'Confidence']] = binary_df_.apply(get_max_confidence, axis=1)
        binary_df_.reset_index(inplace=True)
        binary_df_.rename(columns={'index': 'Organ'}, inplace=True)
        binary_df_['Organ'] = binary_df_['Organ'].str.capitalize()

        # Process triple_df to get the highest confidence
        triple_df_ = triple_df.copy()
        triple_df_[['Predicted', 'Confidence']] = triple_df_.apply(get_max_confidence, axis=1)
        triple_df_.reset_index(inplace=True)
        triple_df_.rename(columns={'index': 'Organ'}, inplace=True)
        triple_df_['Organ'] = triple_df_['Organ'].str.capitalize()

        # Combine binary_df and triple_df
        combined_df = pd.concat([binary_df_, triple_df_], ignore_index=True)

        # Format the 'Predicted' column to have labels as 'Healthy', 'Injured', etc.
        combined_df['Predicted'] = combined_df['Predicted'].str.split('_').str[-1].str.capitalize()

        # Convert the confidence to percentage format
        combined_df['Confidence'] = combined_df['Confidence'].mul(100).round(2)

        combined_df = combined_df[["Organ", "Predicted", "Confidence"]]

        # Rename the columns to match the example output
        combined_df.columns = ['Organ', 'Predicted', 'Confidence (%)']
        output_container.table(combined_df)

        expander = output_container.expander("📝 See inference details")
        expander.info("Below shows the confidence of the model in predicting each class. Confidence is a measure of the model's certainty about its predictions, with higher scores indicating greater certainty. Here, confidence is used to make prediction of the injury class.")
        expander.write("Binary Target Label")
        expander.table(binary_df)

        expander.write("3-Target Label")
        expander.table(triple_df)

        expander.write("Comparison with Ground Truth")
        # load ground truth
        with st.spinner("Loading ground truth data"):
            gt = load_csv()
        t1 = pd.DataFrame.from_dict(inference_result, orient="index", columns=["Prediction"])
        t2 = gt[gt["patient_id"] == int(patient_id)].transpose()

        if len(t2.columns) > 0:
            t2.columns = ["Ground Truth"]
            merged = t1.merge(t2, left_index=True, right_index=True)
            merged['Difference'] = abs(merged["Prediction"] - merged["Ground Truth"])
            expander.table(merged)
        else:
            expander.warning("Ground truth record not found")

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
    st.session_state['patient_id'] = "0"
    st.session_state['series_id'] = "0"
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

def get_max_confidence(row):
    max_confidence = row.max()
    predicted = row.idxmax()
    return pd.Series([predicted, max_confidence], index=['Predicted', 'Confidence'])

main()
