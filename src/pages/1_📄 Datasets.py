import streamlit as st
from widgets.general import normal_text, image, vertical_gap, subtitle, info_card
from util.custom_theme import load_css
import pandas as pd
import pydicom
import os 
from PIL import Image
import re

# Set page configuration for better aesthetics
st.set_page_config(
    page_title="Project RATS | Datasets",
    layout="wide",
    page_icon= Image.open(os.path.join('/mount/src/project-rats/src', 'static', 'favicons', 'favicon-16x16.png'))
)

def main():
    load_css()
    st.header("Datasets")
    normal_text("A <strong>public</strong> competition dataset is used to used to train, validate and test the proposed DL algorithm in the Modelling step. The metadata of the dataset are as below:", style="margin-bottom: 0rem")

    # Dataset provider
    vertical_gap(1)
    image("app/static/imgs/RSNA-Logo.jpg",title="Dataset Provider")  

    # Row 1
    vertical_gap(3)
    subtitle("Collected from", size=5)
    left, right = st.columns(2, gap="medium")

    with left:
        info_card("22", "institutes", left)

    with right:
        info_card("14", "different countries", right)
    
    
    # Row 2
    vertical_gap(3)
    subtitle("Consists of", size=5)
    left, right = st.columns(2, gap="medium")

    with left: 
        info_card("4711", "CT Studies", left)
    
    with right:
        info_card("11", "target labels", right)

    st.divider()

    subtitle("Understanding Data", size=5)
    normal_text("In this dataset, each patient is assigned uniquely with 1 numeric <code>patient_ID</code>. A patient can have multiple <code>series_ID</code>, each corresponding to a different medical procedure or examination. Each <code>series ID</code> contains multiple <code>instance numbers</code>, each representing an individual image within that series. The hierarchical structure is illustrated below:")
    image("app/static/imgs/understanding data.png", style="width:32rem;border-radius:0px") 
    
    # Dataset labels: Dataframe explorer
    vertical_gap(3)
    subtitle("Data Labels", size=5)
    normal_text("<code>train.csv</code> is provided by RSNA and contains target labels for the dataset. Note that patients labeled healthy may still have other medical issues, such as cancer or broken bones, that don't happen to be covered by the competition labels.")
    normal_text("There are 3 target labels (healthy, low, high) for kidney, liver and spleen while 2 target labels (healthy, injury) for bowels and extravasation injury. A binary target label called <code>any injury</code> is also provided to indicate whether the patient has any injury at all.")
    df = pd.read_csv("/mount/src/project-rats/src/assets/train.csv")
    st.dataframe(df, hide_index=True)

    subtitle("Additional metadata", size=5)
    normal_text("Each patient may have been scanned once or twice. Each scan contains a series of images. <code>train_series_meta.csv</code> is provided by RSNA and contains additional metadata for each CT scan series in the dataset.")
    normal_text("")
    df = pd.read_csv("/mount/src/project-rats/src/assets/train_series_meta.csv")
    st.dataframe(df, hide_index=True, use_container_width=True)

    subtitle("Image Dataset Preview", size=5)
    normal_text("Only CT scans of patient 10082, series 8192 is included in this preview. There are a total of 163 CT images in this series.")

    # Directory containing DICOM files
    dicom_directory = "/mount/src/project-rats/src/assets/sample_images/"

    # Custom function to extract number from filename
    def extract_number(filename):
        numbers = re.findall(r'\d+', filename)
        return int(numbers[0]) if numbers else 0

    # # Read DICOM files from the directory and Modify the list comprehension to include custom sorting
    dicom_files = [os.path.join(dicom_directory, f) for f in sorted(os.listdir(dicom_directory), key=extract_number) if f.endswith('.dcm')]
    # dicom_files = [os.path.join(dicom_directory, f) for f in sorted(os.listdir(dicom_directory)) if f.endswith('.dcm')]

    # Initialize or get the current image index
    if 'current_image_idx' not in st.session_state:
        st.session_state.current_image_idx = 0

    # Function to load and return a DICOM image
    def load_dicom_image(file_path):
        print(file_path)
        ds = pydicom.dcmread(file_path)
        img = ds.pixel_array

        # Normalize the image data to 0-255 if it's outside this range
        if img.min() < 0 or img.max() > 255:
            img = img - img.min()  # Shift the image data to start from 0
            img = img / img.max() * 255  # Scale the image data to 0-255
            img = img.astype('uint8')  # Convert to unsigned 8-bit integer

        return img

    # Display the current DICOM image
    if dicom_files:
        # Use columns to center content in the container
        _, _, center_col, _, _ = st.columns([2, 1, 4, 1, 2])
        img = load_dicom_image(dicom_files[st.session_state.current_image_idx])
        center_col.image(img)
        
        vertical_gap(1)

        container = st.container()
        # Buttons to cycle through images
        _,col1, col2, col3,_ = container.columns([2,1,3,1,2])
        with col1:
            if col1.button('Previous', use_container_width=True):
                st.session_state.current_image_idx = (st.session_state.current_image_idx - 1) % len(dicom_files)
        with col2:
            col2.markdown(f"<div class=expand-center>{st.session_state.current_image_idx+1}/{len(dicom_files)}</div>", unsafe_allow_html=True)
        with col3:
            if col3.button('Next', use_container_width=True):
                st.session_state.current_image_idx = (st.session_state.current_image_idx + 1) % len(dicom_files)
    else:
        st.write("No DICOM files found in the specified directory.")

main()