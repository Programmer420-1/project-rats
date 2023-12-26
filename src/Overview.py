import streamlit as st
from widgets.overview import author_card
from widgets.general import normal_text, subtitle, ordered_list, vertical_gap
from util.custom_theme import load_css, load_overview_css, is_dark_theme
from PIL import Image
import streamlit.components.v1 as components
import os

# Set page configuration for better aesthetics
st.set_page_config(
    page_title="Project RATS",
    layout="wide",
    initial_sidebar_state='collapsed',
    page_icon= Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'favicons', 'favicon-16x16.png')),
    menu_items={
        'Report a bug': "mailto:u2102798@siswa.um.edu.my",
        'About': 
        """
        This is a project made for Universiti Malaya Data Science Project 23/24.  

        Created by **Lim Wei Xin**  
        Supervised by **Dr. Hoo Wai Lam**
        """
    }
)




# main executing function
def main():
    load_css()
    load_overview_css()
    # _,center,_ = st.columns([1.5,1,1.5])
    # center.image(Image.open("./static/Logo.png"), use_column_width=True)
    # st.title("Witnessing the new era of abdominal trauma diagnosis: Project <span style='color:red'>RATS</span>")
    # normal_text("Project <strong>R</strong>apid <strong>A</strong>bdominal <strong>T</strong>rauma <strong>S</strong>creening (RATS) is not just another classification model; it's a lifeline. Experience the difference in speed, accuracy, and outcomes as we redefine emergency responses to abdominal trauma.")

    # Call the function
    # dark_theme = is_dark_theme()

    # TODO: Add theme detection and change logo accordingly
    st.markdown(f"""
        <div class='overview-title-container'>
            <div class='logo-container'>
                <img class='logo' src={os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'static', 'Logo_text_hor_sub_dark.png')} alt="Logo"/>    
            </div>
            <span class='h2'>
                Witnessing the <em>new era</em> of abdominal trauma diagnosis: 
            </span>
            <span class='h4'>
                It is not just another classification model; it's a <strong class='blue-text'>lifeline</strong>. 
            </span>
            <span class='h4'>
                Experience the difference in speed, accuracy, and outcomes as we redefine emergency responses to abdominal trauma. 
            </span>
            <a href='#explore'>
                <div class='get-started-frame'>
                    <div class='get-started-container shine'>
                        <span class='h4'>>></span>
                        <span class='h4 get-started-link'>
                            Get Started    
                        </span>
                        <span class='h4'><<</span>
                    </div>
                </div>
            </a>   
        </div>
    """,unsafe_allow_html=True)

    st.divider()

    # Section: Site maps
    st.markdown("""
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.2/css/fontawesome.min.css" integrity="sha384-BY+fdrpOd3gfeRvTSMT+VUZmA728cfF9Z2G42xpaRkUGu2i3DyzpTURDo5A6CaLK" crossorigin="anonymous">
        <div class='title' style='position:relative'>
            <h2 style="visibility:hidden; position:absolute; top:-1rem">Explore</h2>
            <span class='h2'>Explore 🧭</span>
        </div>
        <div class='explore-container'>
            <a href='/Datasets'>
            <div class="card">
                <div class='card-text'>
                    <span class='h6 card-title'>📄 Dataset used</span>
                    <span class='text card-desc'>Dive into the comprehensive dataset that forms the backbone of <span class='project-rats'><span class='project'>Project&nbsp&nbsp</span><span class='rats'>RATS</span></span>. Understand the variables, the data collection process, and the meticulous curation that ensures quality training for our models.</span>
                </div>
                <div class='icon-frame'>
                    <div class='icon-container'>
                        <svg xmlns="http://www.w3.org/2000/svg"  height="16" width="16" viewBox="0 0 512 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.-->
                            <path d="M352 0c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9L370.7 96 201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L416 141.3l41.4 41.4c9.2 9.2 22.9 11.9 34.9 6.9s19.8-16.6 19.8-29.6V32c0-17.7-14.3-32-32-32H352zM80 32C35.8 32 0 67.8 0 112V432c0 44.2 35.8 80 80 80H400c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32V432c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V112c0-8.8 7.2-16 16-16H192c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z"/>
                        </svg>
                    </div>
                </div>
            </div>
            </a>
            <a href='/EDA_&_Model_Comparisons'>
                <div class="card">
                    <div class='card-text'>
                        <span class='h6 card-title'>📊 EDA & Model Comparisons</span>
                        <span class='text card-desc'>Embark on a data exploration journey with our extensive EDA. Uncover patterns, anomalies, and correlations that drive the analytical strategy of <span class='project-rats'><span class='project'>Project&nbsp&nbsp</span><span class='rats'>RATS</span></span>.</span>
                    </div>
                    <div class='icon-frame'>
                        <div class='icon-container'>
                            <svg xmlns="http://www.w3.org/2000/svg"  height="16" width="16" viewBox="0 0 512 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.-->
                                <path d="M352 0c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9L370.7 96 201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L416 141.3l41.4 41.4c9.2 9.2 22.9 11.9 34.9 6.9s19.8-16.6 19.8-29.6V32c0-17.7-14.3-32-32-32H352zM80 32C35.8 32 0 67.8 0 112V432c0 44.2 35.8 80 80 80H400c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32V432c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V112c0-8.8 7.2-16 16-16H192c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z"/>
                            </svg>
                        </div>
                    </div>
                </div>
            </a>
            <a href='/Model_Lab'>
                <div class="card">
                    <div class='card-text'>
                        <span class='h6 card-title'>🔬 Model Lab</span>
                        <span class='text card-desc'>Enter the experimental realm of <span class='project-rats'><span class='project'>Project&nbsp&nbsp</span><span class='rats'>RATS</span></span> where models are tested and tuned. Navigate through performance metrics, tweak parameters, and discover the most effective algorithms for diverse data scenarios.</span>
                    </div>
                    <div class='icon-frame'>
                        <div class='icon-container'>
                            <svg xmlns="http://www.w3.org/2000/svg"  height="16" width="16" viewBox="0 0 512 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.-->
                                <path d="M352 0c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9L370.7 96 201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L416 141.3l41.4 41.4c9.2 9.2 22.9 11.9 34.9 6.9s19.8-16.6 19.8-29.6V32c0-17.7-14.3-32-32-32H352zM80 32C35.8 32 0 67.8 0 112V432c0 44.2 35.8 80 80 80H400c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32V432c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V112c0-8.8 7.2-16 16-16H192c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z"/>
                            </svg>
                        </div>
                    </div>
                </div>
            </a>
        </div>          
    """,unsafe_allow_html=True)

    vertical_gap(2)
    
    # Section: Objectives
    st.markdown("""
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.2/css/fontawesome.min.css" integrity="sha384-BY+fdrpOd3gfeRvTSMT+VUZmA728cfF9Z2G42xpaRkUGu2i3DyzpTURDo5A6CaLK" crossorigin="anonymous">
        <div class='title' style='position:relative'>
            <h2 style="visibility:hidden; position:absolute; top:-1rem">Objectives</h2>
            <span class='h2'><span class='project-rats'><span class='project'>Project&nbsp&nbsp</span><span class='rats'>RATS</span></span> Objectives 🎯</span>
        </div>
        <div class='objectives-container''>
            <div class="card">
                <div class='card-text'>
                    <span class='h6 card-title'>Develop</span>
                    <span class='text card-desc'>Develop an automated system capable of localizing abdominal organs and classifying the severity of trauma.</span>
                </div>
            </div>
            <div class="card">
                <div class='card-text'>
                    <span class='h6 card-title'>Evaluate</span>
                    <span class='text card-desc'>Evaluate existing approaches for classifying severity of abdominal trauma.</span>
                </div>
            </div>
            <div class="card">
                <div class='card-text'>
                    <span class='h6 card-title'>Assemble</span>
                    <span class='text card-desc'>implement a dashboard that optimizes the workload of healthcare providers and offers personalized decision and diagnostic support.</span>
                </div>
            </div>
        </div>          
    """,unsafe_allow_html=True)
    # normal_text("Abdominal trauma presents a significant clinical challenge, especially in emergency situations, as it encompasses a broad range of injuries from minor contusions to life-threatening hemorrhage and organ damage (Barrett and Smith, 2012). Blunt force trauma, which is among the most common types of traumatic injury from motor vehicle accidents can injure multiple organs like the liver, kidneys and spleen, resulting in lesions or bleeding that is potentially fatal (Errol Colak et al., 2023). Patient outcomes are closely correlated with the speed and accuracy of assessing the extent and severity of abdominal trauma. For hemodynamically stable patients with abdominal trauma, findings from Computed Tomography (CT) scans are crucial for healthcare experts to decide on medical procedures to control potentially fatal hemorrhage and optimize resuscitation strategies. With advancements in high-resolution CT imaging, healthcare experts can more accurately gauge trauma severity. However, these potentially lethal injuries are sometimes still overlooked in current practice, as interpreting CT scans for abdominal trauma can be complex and time-consuming, especially with multiple injuries or subtle bleeding (Cheng et al., 2023).")

    # Problem Statements
    # st.subheader("Problem Statements")
    # ordered_list([
    # "Manual interpretation of CT scans for urgent abdominal trauma cases is complex, time-consuming, and not always reliable.",
    # "Radiologists face a heavy burden in interpreting medical images, leading to potential delays and errors.",
    # "The scarcity of radiologists and the absence of automated organ annotation in abdominal imaging present significant challenges in scaling up diagnostic services and advancing deep learning applications."
    # ])

    # # Objectives
    # st.subheader("Objectives of the Project")
    # ordered_list([
    # "To develop an automated system capable of localizing abdominal organs and classifying the severity of trauma.",
    # "To evaluate existing approaches for classifying severity of abdominal trauma.",
    # "To implement a dashboard that optimizes the workload of healthcare providers and offers personalized decision and diagnostic support."
    # ])


    

if __name__ == "__main__":
    container = st.container()
    main()
    # st.sidebar.success("Select a page from above")
