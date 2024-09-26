import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageDraw

from home import display_home 
from projects import display_projects
from proficiencies import display_proficiencies
from work_experience import display_work_experience

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    initial_sidebar_state="collapsed"  # Sidebar initially collapsed
)

# Round corners function
def round_corners(image, radius, background_color=(255, 255, 255)):
    # Create a white background
    background = Image.new('RGB', image.size, background_color)
    
    # Create a mask for rounded corners
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)

    # Apply the mask to the image with the white background
    rounded_img = Image.composite(image, background, mask)
    return rounded_img

# Load and round profile image
img = Image.open("portfolio-pic.jpeg")
radius = 2000  # Large radius for rounded corners
rounded_img = round_corners(img, radius)

# Navbar Styling
navbar_styles = """
    <style>
    .navbar {
        background-color: #1f2937;
        padding: 10px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        font-family: 'Arial', sans-serif;
        font-size: 18px;
    }
    .navbar a {
        color: white;
        padding: 14px 20px;
        text-decoration: none;
        text-align: center;
        border-radius: 4px;
    }
    .navbar a:hover {
        background-color: #4b5563;
        transition: background-color 0.3s ease;
    }
    .navbar .active {
        background-color: #6366f1;
        color: white;
    }
    @media (max-width: 800px) {
        .navbar {
            flex-direction: column;
        }
        .navbar a {
            display: block;
            width: 100%;
        }
    }
    </style>
"""

# Display Navbar
st.markdown(navbar_styles, unsafe_allow_html=True)

# Sidebar option menu
with st.sidebar:
    page = option_menu(
        menu_title="",  
        options=["Home", "Experience", "Projects", "Proficiencies"],  
        icons=["house", "briefcase", "list-task", "tools"],  
        default_index=0 if 'selected_page' not in st.session_state else st.session_state.selected_page,  
        styles={
            "container": {"padding": "5px", "background-color": "#1f2937"},
            "icon": {"color": "white", "font-size": "20px"},  
            "nav-link": {"font-size": "18px", "color": "white", "text-align": "left", "margin": "5px", "border-radius": "5px"},
            "nav-link-selected": {"background-color": "#6366f1"},  
        }
    )

# Check if a new page was selected and trigger rerun to collapse sidebar
if 'selected_page' not in st.session_state or st.session_state.selected_page != ["Home", "Experience", "Projects", "Proficiencies"].index(page):
    st.session_state.selected_page = ["Home", "Experience", "Projects", "Proficiencies"].index(page)
    st.rerun()

# Load the content of the selected page
if page == "Home":
    display_home(rounded_img=rounded_img)
elif page == "Experience":
    display_work_experience()
elif page == 'Projects':
    display_projects()
elif page == "Proficiencies":
    display_proficiencies()

# Additional styling
st.markdown("""
    <style>
    .stImage {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #1f2937;
    }
    .description {
        font-size: 18px;
        color: #4b5563;
        text-align: center;
    }
    .highlight {
        color: #6366f1;
    }
    </style>
""", unsafe_allow_html=True)
