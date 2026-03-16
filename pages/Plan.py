import streamlit as st
from streamlit_calendar import calendar
from translations import get_text
from utils import apply_theme, add_footer,render_sidebar
from data_handler import load_data,save_data
from datetime import datetime, timedelta

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
tab1,tab2 = st.tabs(["Tasks","Calender"])
data = load_data()
with tab1:
    st.subheader("📋 Your Tasks")
    #1.show courses
    if data['courses']:
        for course in data['courses']:
            with st.expander(f"{course['name']} - {course['hours']}h"):
                #progress bar
                progress =  course.get('progress',0)
                st.progress(min(progress/100, 1.0))
                st.write(f"{progress}% Complete")
                #check box for lectures
                lectures_done = st.checkbox("Mark lectures as complete", key=f"complete_{course['name']}")
                #update
                if lectures_done:
                    course['progress'] += (100/course['lectures'])
                    save_data(data)
    else:
        st.write(get_text('no_courses_plan',lang))
    #2.show exams
    st.subheader("📄 Upcoming Exams")
    if data['exams']:
        for exam in data['exams']:
            exam_date_str = exam.get('date', '') 
            # Convert string to datetime object
            exam_date = datetime.strptime(exam_date_str, "%Y-%m-%d")
            days_left = (exam_date - datetime.now()).days
            days_left = max(0, days_left)  # Don't show negative days
            st.write(f"{exam['course']}: {days_left} {get_text('till_exam',lang)} ")
    else:
        st.write(get_text('no_exams',lang))

  
with tab2: 
    st.subheader(get_text("view_plan",lang))
    if not data["courses"]:
        st.warning("⚠️ " + ("Add courses first!" if lang == 'en' else "أضف مواداً أولاً!"))
    else:
        try:
            from streamlit_calendar import calendar
            # Prepare calendar events from your data
            calendar_events = []
            for course in data["courses"]:
                calendar_events.append({
                    "title": f"{course['name']} ({course['hours']}h)",
                    "start": datetime.now().isoformat(),  # You'll need real dates
                    "end": (datetime.now() + timedelta(hours=course['hours'])).isoformat(),
                    "color": "#EF4444" if "🔴" in course.get("priority", "") else "#22C55E"
                })
            
            # Render calendar
            calendar(events=calendar_events, key="study_calendar")
            
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")


