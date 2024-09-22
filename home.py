import streamlit as st
import time


def display_home(rounded_img):
    st.write("##")
    with st.container():
        with st.container():
            st.write("##")
            
            col1, col2, col3, col4 = st.columns([1, 4.5, 2.5, 2])

            with col2:
                st.write("##")
                # Adding a typing effect animation to the title
                st.markdown("""
                <h1 class="title">👋 Hi! I'm Vidhi Kumar, a <span class="highlight">Data Scientist</span>.</h1>
                """, unsafe_allow_html=True)

                # Adding interactive description
                st.markdown("""
                <p class="description">
                    Passionate about uncovering stories hidden within data,<br>
                    I turn raw information into clear, meaningful insights.<br>
                    I enjoy building systems and tools that enable these discoveries,<br>
                    combining <span class="highlight">data engineering</span> and <span class="highlight">analysis</span> to create data-driven solutions.
                </p>
                """, unsafe_allow_html=True)

            with col3:
                st.image(rounded_img, output_format="JPEG", use_column_width="auto")

        # Adding space between sections
        st.write("##")


