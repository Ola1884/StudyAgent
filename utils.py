# utils.py
import streamlit as st

def custom_CSS(lang):
    """Returns custom CSS based on language"""
    font_import = "@import url('https://fonts.googleapis.com/css2?family=Playpen+Sans+Arabic:wght@100..800&display=swap');"
    # Font Family Names & Direction
    if lang == "ar":
        font_family = "'Playpen Sans Arabic', sans-serif"
        direction = "rtl"
        text_align = "right"
    else:
        font_family = "'PT Serif', 'Playpen Sans Arabic', serif"
        direction = "ltr"
        text_align = "left"
    
    CSS = f"""
    <style>
    {font_import}
    
    /* Main App */
    .stApp {{
        background-color: #FFFFFF;
        font-family: {font_family} !important;
        direction: {direction};
        text-align: {text_align};
    }}
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {{
        font-family: {font_family} !important;
        color: #060771;
        font-weight: 700;
    }}
    
    /* Buttons */
    .stButton > button {{
        font-family: {font_family} !important;
        background-color: #9E1C60;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }}
    .stButton > button:hover {{
        background-color: #811844;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }}
    
    /* Input Fields */
    .stTextInput input, 
    .stNumberInput input, 
    .stSelectbox select {{
        font-family: {font_family} !important;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
        direction: {direction};
        text-align: {text_align};
        padding: 8px 12px;
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{
        font-family: {font_family} !important;
        background-color: #060771;
        color: white;
    }}
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {{
        color: white !important;
    }}
    
    /* Cards/Containers */
    .stContainer {{
        background-color: #F3F2EC;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    
    /* Custom Footer */
    .custom-footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F3F2EC;
        color: #060771;
        text-align: center;
        padding: 10px;
        z-index: 9999;
        font-family: {font_family} !important;
        font-size: 0.9rem;
    }}
    
    /* Hide default Streamlit elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
    """
    return CSS

def apply_theme(lang):
    """Applies the theme to the page"""
    st.markdown(custom_CSS(lang), unsafe_allow_html=True)

def add_footer(text):
    """Adds a custom footer"""
    st.markdown(f'<div class="custom-footer">{text}</div>', unsafe_allow_html=True)