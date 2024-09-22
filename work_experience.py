import streamlit as st

def display_work_experience():
    with st.container():
        st.title("Professional Experience I have gathered over the years..")
        st.write("##")
        col1, col2, col3= st.columns([5, 3, 2])

        with col1:
            st.subheader("Persistent Systems Limited")
            # st.write("**SENIOR SOFTWARE ENGINEER**")
            st.markdown("""
            <span class="highlight">**SENIOR SOFTWARE ENGINEER**</span>
                """, unsafe_allow_html=True)
            st.write(
                """
                **Automated ETL Process:**
                - Contributed to a fully automated ETL process.
                - Extracted cloud call usage from Teams, Zoom, and other platforms using API calls to AWS S3, Google BigQuery, and Azure Consumption.
                - Implemented efficient data normalization using PySpark, business logic for rule changes, cost center allocation, and metadata management.
                - Performed data loading using SQL Loader.
                - Managed a web portal delivering live summarized graphs and reports to clients.""")
            st.markdown("""
            <span class="highlight">**SOFTWARE ENGINEER**</span>
                """, unsafe_allow_html=True)
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
            st.markdown("""
            <span class="highlight">**BACKEND DEVELOPER INTERN**</span>
                """, unsafe_allow_html=True)
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
            st.markdown("""
            <span class="highlight">**MENTORSHIP PROGRAM**</span>
                """, unsafe_allow_html=True)
            st.write("""
            - Contributed to creating privacy-preserving machine learning models using federated learning for skin cancer detection.
            """)
        with col2:
            pass
        with col3:
            st.image('psl-logo.png', output_format="PNG")