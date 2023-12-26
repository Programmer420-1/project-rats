import streamlit as st
from widgets.overview import author_card
from widgets.general import normal_text, ordered_list
from util.custom_theme import load_css

# Set page configuration for better aesthetics
st.set_page_config(
    page_title="Project Overview",
)

# main executing function
def main():
    load_css()
    st.header("Abdominal Trauma Classification from CT Scans")
    
    # Author card
    author_card()

    st.divider()

    # Section: Introduction
    st.subheader("Introduction")
    normal_text("Abdominal trauma presents a significant clinical challenge, especially in emergency situations, as it encompasses a broad range of injuries from minor contusions to life-threatening hemorrhage and organ damage (Barrett and Smith, 2012). Blunt force trauma, which is among the most common types of traumatic injury from motor vehicle accidents can injure multiple organs like the liver, kidneys and spleen, resulting in lesions or bleeding that is potentially fatal (Errol Colak et al., 2023). Patient outcomes are closely correlated with the speed and accuracy of assessing the extent and severity of abdominal trauma. For hemodynamically stable patients with abdominal trauma, findings from Computed Tomography (CT) scans are crucial for healthcare experts to decide on medical procedures to control potentially fatal hemorrhage and optimize resuscitation strategies. With advancements in high-resolution CT imaging, healthcare experts can more accurately gauge trauma severity. However, these potentially lethal injuries are sometimes still overlooked in current practice, as interpreting CT scans for abdominal trauma can be complex and time-consuming, especially with multiple injuries or subtle bleeding (Cheng et al., 2023).")

    # Problem Statements
    st.subheader("Problem Statements")
    ordered_list([
    "Manual interpretation of CT scans for urgent abdominal trauma cases is complex, time-consuming, and not always reliable.",
    "Radiologists face a heavy burden in interpreting medical images, leading to potential delays and errors.",
    "The scarcity of radiologists and the absence of automated organ annotation in abdominal imaging present significant challenges in scaling up diagnostic services and advancing deep learning applications."
    ])

    # Objectives
    st.subheader("Objectives of the Project")
    ordered_list([
    "To develop an automated system capable of localizing abdominal organs and classifying the severity of trauma.",
    "To evaluate existing approaches for classifying severity of abdominal trauma.",
    "To implement a dashboard that optimizes the workload of healthcare providers and offers personalized decision and diagnostic support."
    ])


    

if __name__ == "__main__":
    main()
    # st.sidebar.success("Select a page from above")
