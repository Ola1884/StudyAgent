import streamlit as st
from translations import get_text
from utils import apply_theme, add_footer

# ─────────────────────────────────────────────────────────────
# 1. PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────
st.set_page_config(page_title="Wateera",
    page_icon="⏱",
    layout="centered",
    initial_sidebar_state="expanded")
st.text("Start.. Completed✅")
# ─────────────────────────────────────────────────────────────
# 2. INITIALIZE LANGUAGE (Session State)
# ─────────────────────────────────────────────────────────────
if 'language' not in st.session_state:
    st.session_state.language = 'en'
#  Create language switcher button
def toggle_lang():
    if st.session_state.language == 'en':
        st.session_state.language = 'ar'
    else:
        st.session_state.language = 'en'
        
st.button(st.session_state.language,on_click=toggle_lang)
# ─────────────────────────────────────────────────────────────
# 3. SIDEBAR
# ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("Menu")

    st.divider()

# ─────────────────────────────────────────────────────────────
# 4. APPLY THEME (Fonts, Colors, RTL/LTR)
#    MUST be called AFTER language is set
# ─────────────────────────────────────────────────────────────    
apply_theme(st.session_state.language)
lang =  st.session_state.language
# ─────────────────────────────────────────────────────────────
# 5. MAIN CONTENT: Title + Welcome + Navigation Cards
# ─────────────────────────────────────────────────────────────
st.title(get_text('title', lang))
st.write(get_text('welcome', lang))

st.divider()
# Navigation Cards (Two Columns)
col1, col2 = st.columns(2, gap="large")

# Card 1: Setup Courses
with col1:
    with st.container(border=True):
        st.subheader(f" {get_text('setup_courses', lang)}")
        st.write(("Add your courses." if lang == 'en' else "أضف موادك للبدء."))
        if st.button(get_text('setup_courses', lang), key="btn_setup", use_container_width=True):
            st.switch_page("pages/Tasks.py")

# Card 2: View Plan
with col2:
    with st.container(border=True):
        st.subheader(f"🗓️ {get_text('view_plan', lang)}")
        st.write(("View your static plan!" if lang == 'en' else "اعرض خطتك اليدوية!"))
        if st.button(get_text('view_plan', lang), key="btn_plan", use_container_width=True):
            st.switch_page("pages/Plan.py")

col3,col4 = st.columns(2)

# Card 3: Make you own Plan
with col3:
    with st.container(border=True):
        st.subheader(f"📚 {get_text('own_plan', lang)}")
        st.write(("Add your courses." if lang == 'en' else "أضف موادك للبدء."))
        if st.button(get_text('own_plan', lang), key="btn_setup", use_container_width=True):
            st.switch_page("pages/Static_generator.py")
with col4:
    with st.container(border=True):
        st.subheader(f"📚 {get_text('ai_planner', lang)}")
        st.write(("Add your courses." if lang == 'en' else "أضف موادك للبدء."))
        if st.button(get_text('ai_planner', lang), key="btn_setup", use_container_width=True):
            st.switch_page("pages/Generator.py")


# ─────────────────────────────────────────────────────────────
# 6. CUSTOM FOOTER
# ─────────────────────────────────────────────────────────────
add_footer(get_text('footer', lang))