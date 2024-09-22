import streamlit as st
import base64

# Function to convert image to base64
def get_image_as_base64(image_path):
    with open(image_path, "rb") as file:
        image_data = file.read()
    return base64.b64encode(image_data).decode()

def display_projects():
    with st.container():
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(
                    """
                    <div style="text-align: center;">
                        <h3>Learning the World with Olympic Data</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                img_path = "olympic-pic.jpeg"  # Local path in your project folder
                link_url = "https://github.com/vidhi-kumar/olympic-insights/blob/main/olympics-analysis.ipynb"
                img_base64 = get_image_as_base64(img_path)
                st.markdown(f"""
                    <style>
                    .image-container {{
                        display: inline-block;
                        position: relative;
                        text-align: center; /* Center the image */
                    }}

                    .image-container img {{
                        transition: transform 0.3s ease;
                        border-radius: 8px;
                    }}

                    .image-container img:hover {{
                        transform: scale(1.1);
                    }}

                    .image-container .click-indicator {{
                        position: absolute;
                        top: 80%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        color: white;
                        background-color: rgba(0, 0, 0, 0.5);
                        padding: 5px 10px;
                        border-radius: 5px;
                        font-size: 14px;
                        text-align: center;
                        opacity: 1;
                        transition: opacity 0.3s ease;
                    }}

                    .image-container:hover .click-indicator {{
                        opacity: 0;
                        pointer-events: none;
                    }}

                    /* Center the image container itself */
                    .center {{
                        display: flex;
                        justify-content: center;
                    }}
                    </style>

                    <div class="center">
                        <div class="image-container">
                            <a href="{link_url}" target="_blank">
                                <img src="data:image/jpeg;base64,{img_base64}" alt="Olympic Data Analysis" width="300">
                            </a>
                            <div class="click-indicator">Click to view project</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                st.write("<br>", unsafe_allow_html=True)
                st.markdown("Explored Olympic data (1896-2024), **revealing global trends and actionable insights.**", unsafe_allow_html=True)
                st.markdown("""
                Utilized <span class="highlight">**python, pandas**</span> and <span class="highlight">**matplotlib**</span>
                for data analysis and visualization.
                """, unsafe_allow_html=True)
        
            with col2:
                st.markdown(
                    """
                    <div style="text-align: center;">
                        <h3>API Playground</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                img_path = "playground-api.jpeg"  # Local path in your project folder
                link_url = "https://github.com/vidhi-kumar/playgroundAPI"
                img_base64 = get_image_as_base64(img_path)
                st.markdown(f"""
                    <style>
                    .image-container {{
                        display: inline-block;
                        position: relative;
                        text-align: center; /* Center the image */
                    }}

                    .image-container img {{
                        transition: transform 0.3s ease;
                        border-radius: 8px;
                    }}

                    .image-container img:hover {{
                        transform: scale(1.1);
                    }}

                    .image-container .click-indicator {{
                        position: absolute;
                        top: 80%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        color: white;
                        background-color: rgba(0, 0, 0, 0.5);
                        padding: 5px 10px;
                        border-radius: 5px;
                        font-size: 14px;
                        text-align: center;
                        opacity: 1;
                        transition: opacity 0.3s ease;
                    }}

                    .image-container:hover .click-indicator {{
                        opacity: 0;
                        pointer-events: none;
                    }}

                    /* Center the image container itself */
                    .center {{
                        display: flex;
                        justify-content: center;
                    }}
                    </style>

                    <div class="center">
                        <div class="image-container">
                            <a href="{link_url}" target="_blank">
                                <img src="data:image/jpeg;base64,{img_base64}" alt="Playground APIs" width="300">
                            </a>
                            <div class="click-indicator">Click to view project</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                st.write("<br>", unsafe_allow_html=True)
                st.markdown("""Containerized API testing environment built with <span class="highlight">**FastAPI**</span> and 
                            <span class="highlight">**JWT**</span> authentication.
                            """, unsafe_allow_html=True)
                st.markdown("""Isolated dashboard to experiment with APIs, using <span class="highlight">**SQLite**</span> and <span class="highlight">**Docker**</span> for easy 
                        local testing and built-in <span class="highlight">**Swagger**</span> documentation.""", unsafe_allow_html=True)
                