import streamlit as st
from widgets.general import normal_text, subtitle, vertical_gap
from util.custom_theme import load_css
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from widgets.eda import binary_class_distribution \
    , multiclass_class_distribution \
    , n_scans_per_study, correlation_heat_map \
    , slice_thickness_distribution
from PIL import Image

import os

# Set page configuration for better aesthetics
st.set_page_config(
    page_title="Project RATS | EDA",
    layout="wide",
    page_icon= Image.open("./static/favicons/favicon-16x16.png")
)

def main():

    print(os.listdir())
    load_css()
    st.header("Exploratory Data Analysis (EDA)")
    normal_text("The main idea of EDA is to harvest the interesting pattern and relations among the variables in the dataset (IBM, 2020). Below covers all the visualization of EDA techniques done to the dataset.", style="margin-bottom:-1.618rem")
    
    st.divider()

    ## Plotting
    # Number of scans
    subtitle("Number of Scans per Series/Studies", size=5)
    n_scans_per_study()

    # Class Distribution
    vertical_gap(2)
    subtitle("Class Distribution", size=5)
    subtitle("Binary Target Organs", size=6)
    binary_class_distribution()

    subtitle("3-Target Organs", size=6)
    multiclass_class_distribution()

    # Correlation Heat map
    vertical_gap(2)
    subtitle("Correlation Heat Map Between Organs", size=5)
    correlation_heat_map()

    # Correlation Heat map
    vertical_gap(2)
    subtitle("Study Slice Thickness Distribution", size=5)
    slice_thickness_distribution()

main()