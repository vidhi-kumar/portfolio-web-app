import streamlit as st
import time


def display_home(rounded_img):
    with st.container():
        # st.write("##")
        
        col1, col2 = st.columns([6, 4])

        with col1:
            # st.write("##")
            # Adding a typing effect animation to the title
            st.markdown("""
            <h1 class="title">Hello Universe 👋 I'm Vidhi Kumar, a <span class="highlight">Data Scientist</span>.</h1>
            """, unsafe_allow_html=True)

            # Adding interactive description
            st.markdown("""
            <p class="description">
                Passionate about uncovering stories hidden within data,
                I turn raw information into clear, meaningful insights.
                I enjoy building systems and tools that enable these discoveries,
                combining <span class="highlight">data engineering</span> and <span class="highlight">analysis</span> to create data-driven solutions.
            </p>
            """, unsafe_allow_html=True)

        with col2:
            # st.write("##")
            st.image(rounded_img, output_format="JPEG", use_column_width="auto")

    # Adding horizontal line 
    # st.write("---")
    st.write("##")

 # HTML for the heading
    # st.markdown("""
    #     <div>
    #         <h3 style="text-align: center; color: #666;">Catch Up on My Latest Projects..</h3>
    #     </div>
    # """, unsafe_allow_html=True)
    # Streamlit button styled via HTML and connected to navigation logic
    if st.button("Recent Work", key="projects_button"):
        st.session_state.selected_page = 2  # Set 'Projects' as the selected page
        st.rerun()  # Trigger a page rerun to update the selected page

    # Additional styling for the Streamlit button
    st.markdown("""
    <style>
    div.stButton > button {
        background-color: transparent; /* Transparent background */
        color: #4b4b4b; /* Dark gray text */
        padding: 10px 20px;
        font-size: 16px; /* Slightly smaller font */
        border-radius: 4px; /* Subtle rounding */
        border: none;
        cursor: pointer;
        display: block;
        margin: auto;  /* Center the button */
        transition: background-color 0.3s, color 0.3s, transform 0.3s, box-shadow 0.3s; /* Smooth transitions */
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* Sharp shadow to the right and bottom */
        outline: none;
    }
    div.stButton > button:hover {
        background-color: #D3D3D3; /* Change background on hover */
        color: black; /* Change text color on hover */
        box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.5); /* Increase shadow on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# adding handles
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://www.linkedin.com/in/vidhi-kumar/" style="text-decoration: none; margin: 0 10px;">
                <i class="fab fa-linkedin" style="font-size: 24px; color: #4b4b4b;"></i>
            </a>
            <a href="https://github.com/vidhi-kumar" style="text-decoration: none; margin: 0 10px;">
                <i class="fab fa-github" style="font-size: 24px; color: #4b4b4b;"></i>
            </a>
        </div>
    """, unsafe_allow_html=True)