import streamlit as st

def display_home(rounded_img):
    with st.container():
            # st.title(":wave: Hi! I'm Vidhi Kumar, a Data Scientist.")
            st.write("##")
            st.write("##")

            col1, col2,col3,col4 = st.columns([1,4.5,2.5,2])
            with col2:
                # st.write("##")
                st.title(":wave: Hi! I'm Vidhi Kumar, a Data Scientist.")
                st.write("""
                Passionate about uncovering stories hidden within data,<br>
                I turn raw information into clear, meaningful insights. <br>
                I enjoy building the systems and tools that help make these discoveries possible, <br>
                bringing together data engineering and analysis to create practical, data-driven solutions.
                """, unsafe_allow_html=True)
            with col3:
                # with st.spinner("..."):
                    # st.image(rounded_img, output_format="PNG", use_column_width="auto")
                st.image(rounded_img, output_format="JPEG", use_column_width="auto")