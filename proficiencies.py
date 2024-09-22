import streamlit as st

def display_proficiencies():
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