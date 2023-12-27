import streamlit as st

def author_card():
    container = st.container()
    container.markdown("""
        <div class=author-card> 
            <img class=profile-pic src="app/static/profile_pic.jpg" alt="profile picture"/>
            <div class=author-info>
                <span><strong>Lim Wei Xin</strong></span>
                <span>Universiti Malaya</span>
            </div>
        </div>
    """, unsafe_allow_html=True)



        
        