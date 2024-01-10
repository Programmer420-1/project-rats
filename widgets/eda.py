import streamlit as st
from widgets.general import normal_text
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import os

df = pd.read_csv(os.path.join('assets', 'dataset_summary.csv'))
df_dicom = pd.read_parquet(os.path.join('assets', 'train_dicom_tags.parquet'))

@st.cache_data
def n_scans_per_study():
    fig, ax = plt.subplots(figsize=(15,10))
    sns.histplot(df['num_scans'],kde=True, ax=ax, color="#2078b3",line_kws={'color': '#ff0134'}, bins=50, alpha=0.8)
    fig.patch.set_alpha(0)
    ax.set_facecolor((0, 0, 0, 0))
    ax.yaxis.grid(True, color='gray')  # Show horizontal grid lines in gray color
    ax.xaxis.label.set_color('white')   # Set x-axis label color to gray
    ax.yaxis.label.set_color('white')   # Set y-axis label color to gray

    ax.set_xlabel('Number of Scans', fontsize=16, fontweight=600)
    ax.set_ylabel('Count', fontsize=16, fontweight=600)

    # Change the color of the axes themselves to gray
    ax.tick_params(axis='x', colors='gray', labelsize=14)  # Change x-axis ticks to gray
    ax.tick_params(axis='y', colors='gray', labelsize=14)  # Change y-axis ticks to gray

    ax.lines[0].set_color('#ff0134')

    for spine in ax.spines.values():
        spine.set_visible(False)
        
    # Display in Streamlit
    _, center, _ = st.columns([1,3,1])
    center.pyplot(fig)
    normal_text("From the graph, it illustrated the dataset shows a significant concentration of studies around <strong>168</strong> and <strong>668</strong> number of scans. This notable pattern persists even when the data is grouped into large intervals of 50, whereby highlighting these values as key measurements within the dataset.")

@st.cache_data
def binary_class_distribution():
    selected_organs = ["extravasation", "bowel"]
    stacked_data = df[selected_organs].apply(pd.Series.value_counts).fillna(0).T

    # Step 3: Convert the counts to percentages
    stacked_data_percent = stacked_data.div(stacked_data.sum(axis=1), axis=0) * 100

    # Step 4: Plot and style the horizontal stacked bar chart
    fig, ax = plt.subplots(figsize=(15, 5))
    stacked_data_percent.plot(kind='barh', stacked=True, color=['#2078b3', '#ff0134'], ax=ax, zorder=3)

    # Advanced Styling
    fig.patch.set_alpha(0)
    ax.set_facecolor((0, 0, 0, 0))
    ax.xaxis.grid(True, color='gray', linestyle='-', linewidth=0.7, zorder=0)  # Grid behind bars
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.set_xlabel('Percentage', fontsize=16, fontweight='bold')
    ax.tick_params(axis='y', colors='gray', labelsize=14)
    ax.tick_params(axis='x', colors='gray', labelsize=14)
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.yticks(rotation=90, va="center")
    plt.legend(title='Injury Level', labels=['[0] Healthy', '[1] Injured'], loc='lower left')

    _, center, _ = st.columns([1,4,1])
    center.pyplot(fig)
    # Rename 
    stacked_data_percent.columns = ['[0] Healthy', '[1] Injured']
    center.table(stacked_data_percent)
    # normal_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget lorem libero. Ut ullamcorper congue nulla, quis mattis purus ullamcorper vitae. Aenean accumsan metus ut faucibus iaculis. Sed vitae enim eget diam tincidunt fermentum sit amet et erat. Vestibulum aliquam pulvinar nibh, et tempor lorem.")

@st.cache_data
def multiclass_class_distribution():
    selected_organs = ["spleen", "liver", "kidney"]
    stacked_data = df[selected_organs].apply(pd.Series.value_counts).fillna(0).T

    # Step 3: Convert the counts to percentages
    stacked_data_percent = stacked_data.div(stacked_data.sum(axis=1), axis=0) * 100

    # Step 4: Plot and style the horizontal stacked bar chart
    fig, ax = plt.subplots(figsize=(15, 5))
    stacked_data_percent.plot(kind='barh', stacked=True, color=['#2078b3', '#ff0134', '#852542'], ax=ax, zorder=3)

    # Advanced Styling
    fig.patch.set_alpha(0)
    ax.set_facecolor((0, 0, 0, 0))
    ax.xaxis.grid(True, color='gray', linestyle='-', linewidth=0.7, zorder=0)  # Grid behind bars
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.set_xlabel('Percentage', fontsize=16, fontweight='bold')
    ax.tick_params(axis='y', colors='gray', labelsize=14)
    ax.tick_params(axis='x', colors='gray', labelsize=14)
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.yticks(rotation=90, va="center")
    plt.legend(title='Injury Level', labels=['[0] Healthy', '[1] Injured_Low', '[2] Injured_High'], loc='lower left')
    
    _, center, _ = st.columns([1,4,1])
    center.pyplot(fig)
    # normal_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget lorem libero. Ut ullamcorper congue nulla, quis mattis purus ullamcorper vitae. Aenean accumsan metus ut faucibus iaculis. Sed vitae enim eget diam tincidunt fermentum sit amet et erat. Vestibulum aliquam pulvinar nibh, et tempor lorem.")
    # Rename
    stacked_data_percent.columns = ['[0] Healthy', '[1] Injured_Low', '[2] Injured_High']
    center.table(stacked_data_percent)

@st.cache_data
def correlation_heat_map():
    # Select interested variables
    interested_variables = ["extravasation", "bowel", "kidney", "liver", "spleen"]
    correlation_data = df[interested_variables]

    # Calculate correlation matrix
    correlation_matrix = correlation_data.corr()

    # Create a custom colormap
    colors = ['#2078b3', '#ff0134']  # Blue to Red
    n_bins = 1000  # Increase this number for a smoother transition
    cmap = LinearSegmentedColormap.from_list("custom_colormap", colors, N=n_bins)

    scale = 1.25
    # Generate heatmap
    plt.figure(figsize=(10 * scale, 8 * scale))
    sns.heatmap(correlation_matrix, annot=True, cmap=cmap, fmt=".2f", linewidths=2.5, annot_kws={"size": 14, "weight": 800})
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.gca().patch.set_alpha(0)
    plt.gca().set_facecolor((0, 0, 0, 0))
    plt.gca().tick_params(axis='both', colors='gray', labelsize=14)
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    _, center, _ = st.columns([1,3,1])
    center.pyplot(plt, transparent=True)
    normal_text("The correlation heatmap shows that there exist only <strong>weak correlations</strong> in organ-organ and organ-extravasation pairs. The highest correlation coefficient is <strong>0.18</strong> and can be observed from pair <em>Kidney-Liver</em> and <em>Spleen-Extravasation</em>.")

@st.cache_data
def slice_thickness_distribution():
    # Gest series folder
    df_dicom["PatientID"] = df_dicom["PatientID"].astype(str)
    df_dicom["series"] = df_dicom["SeriesInstanceUID"].apply(lambda x: x.split(".")[-1])
    df_dicom['PatientID_series'] = df_dicom['PatientID'].astype(str) + '_' + df_dicom['series'].astype(str)

    # Remove duplicates based on the 'PatientID_series' column
    df_unique = df_dicom.drop_duplicates(subset='PatientID_series')
    df_unique = df_unique[["PatientID", "series", "SliceThickness"]]

    df_extracted = df_unique.groupby("SliceThickness").count()["series"]
    # Sort the Series by its values in descending order
    df_extracted_sorted = df_extracted.sort_values(ascending=False)

    # Creating a numerical range for the x-axis positions
    x_positions = np.arange(len(df_extracted_sorted))

    plt.figure(figsize=(15, 8))

    # Plotting the bar chart using numerical x positions
    plt.bar(x_positions, df_extracted_sorted.values, color='#2078b3', zorder=1 )

    # Setting the x-ticks to be at these numerical positions
    plt.xticks(x_positions, df_extracted_sorted.index, rotation=45, ha='right')

    # Setting labels and title
    plt.xlabel('Slice Thickness (mm)',fontsize=14, fontweight='bold')
    plt.ylabel('Count',fontsize=14, fontweight='bold')

    # Additional styling
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.gca().patch.set_alpha(0)
    plt.gca().set_facecolor((0, 0, 0, 0))
    plt.gca().yaxis.grid(True, color='gray', linestyle='-', linewidth=0.7, zorder=0)
    plt.gca().tick_params(axis='both', colors='gray', labelsize=14)
    plt.gca().yaxis.label.set_color('white')
    plt.gca().xaxis.label.set_color('white')
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    _, center, _ = st.columns([1,3,1])
    center.pyplot(plt, transparent=True)
    normal_text("The bar chart show the distribution of slice thickness of every study in the provided dataset. The result shows that the thickess of the studies within the datset is not consistent. This may be due to the data are collected from different machines or equipments of different countries and institutes. From the distribution, 3.0mm is the most common thickness while 1.0mm follows after.")

@st.cache_data
def load_csv(path=os.path.join('assets', 'ground_truth.csv')):
    data = pd.read_csv(path)
    return data