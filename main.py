import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageDraw

from home import display_home 
from projects import display_projects
from proficiencies import display_proficiencies
from work_experience import display_work_experience

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

# Load and process the image (avoid using PNG for faster rendering)
img = Image.open("portfolio-pic.jpeg")
radius = 2000  # large value to make the image round
rounded_img = round_corners(img, radius)

# Sidebar with option_menu for navigation
with st.sidebar:
    page = option_menu(
        menu_title="Main Menu",  # required
        options=["Home", "Work Experience", "Projects", "Proficiencies"],  # options for the nav
        icons=["house", "briefcase", "list-task", "tools"],  # optional icons from Bootstrap
        menu_icon="cast",  # optional icon for the menu
        default_index=0,  # default selected menu item
    )

# Inject JavaScript to collapse the sidebar on every menu selection (for mobile and desktop)
st.markdown("""
    <script>
    // Function to collapse the sidebar after menu selection
    function collapseSidebar() {
        var sidebar = parent.document.querySelector('[data-testid="stSidebar"]');
        var closeButton = parent.document.querySelector('button[aria-label="Close"]');
        if (sidebar && closeButton && sidebar.style.width !== '0px') {
            closeButton.click();  // Simulate the close button click
        }
    }

    // Attach the function to the menu item click event
    var menuItems = parent.document.querySelectorAll(".css-1v3fvcr a");
    menuItems.forEach(function(menuItem) {
        menuItem.addEventListener('click', collapseSidebar);  // Collapse sidebar on every click
    });
    </script>
""", unsafe_allow_html=True)

# Handle navigation
if page == "Home":
    display_home(rounded_img=rounded_img)

if page == "Work Experience":
    display_work_experience()

if page == 'Projects':
    display_projects()
        
if page == "Proficiencies":
    display_proficiencies()

# Additional styling for image and titles
st.markdown("""
    <style>
    .stImage {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
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
