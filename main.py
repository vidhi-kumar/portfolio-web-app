import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
from PIL import Image, ImageOps
from PIL import ImageDraw
from streamlit_lottie import st_lottie
import requests
import json
import time
import base64

from home import display_home 

from projects import display_projects

from proficiencies import display_proficiencies

from work_experience import display_work_experience

st.set_page_config(layout="wide")

# st.markdown("<style>.element-container{opacity:1 !important}</style>", unsafe_allow_html=True)


@st.cache_data
def load_image(image_path):
    return Image.open(image_path)

def load_lottie_url(url: str) -> json:
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




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


# avoid using png pics because they are slower to render (due to its compression)
img = Image.open("portfolio-pic.jpeg")
radius = 2000  # a large value will make the image round
rounded_img = round_corners(img, radius)



page = st_navbar(["Home", "Work Experience", "Projects", "Proficiencies", "Contact me"])

lottie_coder = load_lottie_url("https://lottie.host/12b4aa73-2751-432e-aceb-a4de8134d10f/mORuoSlkIW.json")

if page == "Home":
    display_home(rounded_img=rounded_img)

if page == "Work Experience":
    display_work_experience()

if page == 'Projects':
    display_projects()
        
if page == "Proficiencies":
    display_proficiencies()

# Additional styling for the entire page
st.markdown("""
    <style>
    .stImage {
        animation: fadeIn 2s ease-in-out;
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