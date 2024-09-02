import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
from PIL import Image, ImageOps
from PIL import ImageDraw
from streamlit_lottie import st_lottie
import requests
import json
import time

st.set_page_config(layout="wide")


def load_lottie_url(url: str) -> json:
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def round_corners(image, radius):
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result

img = Image.open("portfolio-pic.jpeg")
# img = Image.open("portfolio-pic-2.jpeg")
# img = Image.open("pic4.png")
radius = 2000  # You can adjust the radius as needed
rounded_img = round_corners(img, radius)


page = st_navbar(["Home", "Work Experience", "Projects", "Proficiencies", "Contact me"])

lottie_coder = load_lottie_url("https://lottie.host/12b4aa73-2751-432e-aceb-a4de8134d10f/mORuoSlkIW.json")
# st.write("##") #blank space

# st.subheader("Welcome :wave:")
# title
# st.title(":wave: Hi! I'm Vidhi Kumar, a Data Scientist.")
# navigation menu
# with st.container():
#     selected = option_menu(
#         menu_title = None,
#         options = ['About', 'Projects', 'Contact'],
#         icons = ['person', 'code-slash', 'chat-left-text-fill'],
#         orientation = "horizontal"
#     )
if page == "Home":
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
            st.image(rounded_img, output_format="PNG", use_column_width="auto")


if page == "Work Experience":
    with st.container():
        st.title("Professional Experience I have gathered over the years..")
        st.write("##")
        col1, col2, col3= st.columns([5, 3, 2])

        with col1:
            st.subheader("Persistent Systems Limited")
            st.write("**SENIOR SOFTWARE ENGINEER**")
            st.write(
                """
                **Automated ETL Process:**
                - Contributed to a fully automated ETL process.
                - Extracted cloud call usage from Teams, Zoom, and other platforms using API calls to AWS S3, Google BigQuery, and Azure Consumption.
                - Implemented efficient data normalization using PySpark, business logic for rule changes, cost center allocation, and metadata management.
                - Performed data loading using SQL Loader.
                - Managed a web portal delivering live summarized graphs and reports to clients.""")
            st.write("**SOFTWARE ENGINEER**")
            st.write("""
                **Tangoe Usage Management Project:**
                - Part of the Tangoe Usage Management project, which processes call records and generates invoices for over 25 clients.
                - Achieved over 85% optimization in critical data processing, reducing time from 46 hours to 6 hours.
                - Applied Exploratory Data Analysis (EDA) on Call Data Records to determine patterns in call duration and peak hours.
                - Utilized time series analysis to uncover evolving call patterns over different time intervals.

                **Sports Inventory Management APIs** < Proof of Concept >:
                - Developed Sports Inventory Management APIs with authenticated endpoints for a client's Proof of Concept.
                - Utilized Docker containerization for easy local deployment and connected to a relational database.
                - Implemented FastAPI for API creation, Swagger for documentation, and secure access with JWT token authentication.

                **Sentiment Analysis** < Proof of Concept >:
                - Achieved 86% accuracy working on an MLOps-driven sentiment analysis Proof of Concept utilizing Twitter data.
                - Incorporated distributed data processing and model training, along with reproducibility and deployment.
                """)
        
        with col2:
            pass
        with col3:
            st.image('psl-logo.png', output_format="PNG")
        
        st.write("##")
        col1, col2, col3= st.columns([5, 3, 2])
        with col1:
            st.subheader("Spintly")
            st.write("**BACKEND DEVELOPER INTERN**")
            st.write("""
            - Created software to replicate client experience at Spintly using API calls to Spintly Backend.
            - Extensively worked on Node.js/Express with PostgreSQL and AWS Lambda for REST API development.
            """)
        with col2:
            # st.write("--- May 2022 - June 2022")
            pass
        with col3:
            st.image('spintly-logo.jpeg', output_format="PNG")

        st.write("##")
        col1, col2, col3= st.columns([5, 3, 2])
        with col1:
            st.subheader("Persistent Systems Limited")
            st.write("**MENTORSHIP PROGRAM**")
            st.write("""
            - Contributed to creating privacy-preserving machine learning models using federated learning for skin cancer detection.
            """)
        with col2:
            pass
        with col3:
            st.image('psl-logo.png', output_format="PNG")


if page == "Proficiencies":
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Data Science")
            st.write("""
            - **Federated Learning:** Contributed to privacy-preserving machine learning models for skin cancer detection.
            - **MLOps:** Experience with MLOps-driven sentiment analysis using distributed data processing and model training.
            - **Exploratory Data Analysis (EDA):** Applied EDA techniques to uncover patterns and trends in large datasets.
            - **PySpark:** Efficient data normalization and processing of large datasets.
            - **Visualization:** Created live summarized graphs and reports for clients using various tools and technologies.
            """)

        with col2:
            st.subheader("Backend Development & Tools")
            st.write("""
            - **FastAPI:** Developed secure APIs with JWT authentication and documented with Swagger.
            - **Docker:** Containerization for consistent environments and deployment.
            - **AWS & BigQuery:** Utilized AWS S3, Lambda, and Google BigQuery for data processing and API development.
            - **ETL Automation:** Automated ETL processes using AWS S3, Google BigQuery, and Azure Consumption.
            """)

        with col3:
            st.subheader("Programming Languages")
            st.write("""
            - **Python:** Extensive experience in data processing, ETL automation, and API development.
            - **Node.js:** Proficient in developing REST APIs using Node.js and Express.
            - **SQL:** Skilled in SQL for data extraction, normalization, and loading, particularly with PostgreSQL and SQL Loader.
            """)

        # Add some spacing for better layout
        st.write("---")

        st.write("This section presents a snapshot of my technical proficiencies, categorized to highlight my experience in different domains.")
        # col1, col2,col3 = st.columns(3)
        # with col1:
        #     st.image('python-logo.jpeg', output_format="PNG")
        # with col2:
        #     st.image('sql-logo.png', output_format="PNG")
        # with col3:
        #     st.image('pandas-logo.png', output_format="PNG")
        
        # col1, col2,col3 = st.columns(3)
        # with col1:
        #     st.image('powerbi-logo.png', output_format="PNG")
        # with col2:
        #     st.image('streamlit-logo.png', output_format="PNG")
        # with col3:
        #     st.image('matplotlib-logo.png', output_format="PNG")



# byline
# st.write("""
#         Passionate about uncovering stories hidden within data, 
#          I turn raw information into clear, meaningful insights. <br>
#          I enjoy building the systems and tools that help make these discoveries possible, 
#          bringing together data engineering and analysis <br>  to create practical, data-driven solutions.
#          """, unsafe_allow_html=True)

# horizontal break
# st.write("---")

# navigation menu
# with st.container():
#     selected = option_menu(
#         menu_title = None,
#         options = ['About', 'Projects', 'Contact'],
#         icons = ['person', 'code-slash', 'chat-left-text-fill'],
#         orientation = "horizontal"
#     )

# if selected == "About":
#     with st.container():
#         col1, col2 = st.columns([7.5, 2.5])
#         with col1:
#             st.write("##")
#             st.subheader("Senior Software Engineer")
#             st.write("Persistent Systems Limited (August 2022 - Present)")
#             st.write("##")
#             st.subheader("Backend Developer Intern")
#             st.write("Spintly")
#         with col2:
#             st.write("##")
#             st_lottie(lottie_coder)

