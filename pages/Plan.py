import streamlit as st
from streamlit_calendar import calendar
from translations import get_text
from utils import apply_theme, add_footer,render_sidebar
from data_handler import load_data,save_data
import datetime
# ─────────────────────────────────────────────────────────────
# 1. PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="View Plan",
    page_icon="🗓️",
    layout="centered"
)
# ─────────────────────────────────────────────────────────────
# 2. GET LANGUAGE
# ─────────────────────────────────────────────────────────────
if 'language' not in st.session_state:
    st.session_state.language = 'en'
lang = st.session_state.language
# ─────────────────────────────────────────────────────────────
# 3. SIDEBAR: Back Button + Language Toggle
# ─────────────────────────────────────────────────────────────  
render_sidebar(lang,show_back_button=True)
# ─────────────────────────────────────────────────────────────
# 4. APPLY THEME
# ─────────────────────────────────────────────────────────────
apply_theme(lang)
#______________________________________________________________
# 5. TABS: LIST & CALENDER VIEW
#______________________________________________________________
tab1,tab2 = st.tabs(["List of Tasks","Calender"])
data = load_data()
with tab1:
    st.subheader("📋 Your Study Tasks")
    #1.show courses
    for course in data["courses"]:
        with st.expander(f"{course['name']} - {course['hours']}h"):
            #progress bar
            progress =  course.get('progress',0)
            st.progress(progress/100)
            #check box for lectures
            lectures_done = st.checkbox("Mark lectures as complete")
            #update
            if lectures_done:
                course['progress'] += (100/course['lectures'])
                save_data(data)
    #2.show exams
    st.subheader("📄 Upcoming Exams")
    for exam in data['exams']:
        days_left = (exam['exam_date']- (datetime.datetime.now()))
        st.write(f"{exam['course']}: {days_left} {get_text('till_exam',lang)} ")

calendar_options = {
    "editable": True,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "building",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},
        {"id": "b", "building": "Building A", "title": "Building B"},
        {"id": "c", "building": "Building B", "title": "Building C"},
        {"id": "d", "building": "Building B", "title": "Building D"},
        {"id": "e", "building": "Building C", "title": "Building E"},
        {"id": "f", "building": "Building C", "title": "Building F"},
    ],
}
calendar_events = [
    {
        "title": "Event 1",
        "start": "2023-07-31T08:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "start": "2023-07-31T07:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "a",
    }
]
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""

calendar = calendar(
    events=calendar_events,
    options=calendar_options,
    custom_css=custom_css,
    key='calendar', 
    )
with tab2: 
    st.subheader(get_text("view_plan",lang))
    st.write(calendar)
