import streamlit as st
import json
import os
from translations import get_text
from utils import apply_theme, add_footer,render_sidebar
from data_handler import load_data,save_data

# ─────────────────────────────────────────────────────────────
# 1. PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Setup Tasks",
    page_icon="📚",
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
# ───────────────────────────────────────────────────────────── " ➞ "," ⬅ " 
render_sidebar(lang,show_back_button=True)
# ─────────────────────────────────────────────────────────────
# 4. APPLY THEME
# ─────────────────────────────────────────────────────────────
apply_theme(lang)
# ─────────────────────────────────────────────────────────────
# 5. DATA HANDLING (JSON File)
# ─────────────────────────────────────────────────────────────
#load current data
data = load_data()  
# ─────────────────────────────────────────────────────────────
# 6. MAIN CONTENT: Title + Forms
# ─────────────────────────────────────────────────────────────
st.title(get_text('task_title',lang))
# 7. Input Form
with st.form("task_form"):
    col1, col2, col3,col4 = st.columns(4)
    
    with col1:
        course_name = st.text_input(get_text("course_name",lang), placeholder="e.g., Math")
    with col2:
        hours = st.number_input(get_text("hours_per_day",lang), min_value=0.5, max_value=12.0, step=0.5)
    with col3:
        lectures = st.number_input(get_text("lectures",lang),min_value=0,step=1)
    with col4:
        priority = st.selectbox(get_text("priority",lang), ["High 🔴", "Medium 🟡", "Low 🟢"]  if lang == "en" else ["🔴عالي ", "🟡متوسط ", "🟢منخفض "])

    
    submitted_course = st.form_submit_button(get_text("add_course",lang))

    # 8. Logic to Save Task
    if submitted_course and course_name:
        if any(c['name'] == course_name for c in data['courses']):
            st.warning(f"⚠️ {course_name}" + "already exists!!!" if lang == 'en' else "موجود مسبقا!!!")
        else:
            data["courses"].append({
                "name": course_name,
                "hours": hours,
                "lectures":lectures,
                "progress": 0
            })
            save_data(data)
            st.success(get_text('added_success', lang).format(course_name))
            st.rerun()
st.divider()
# ─────── SECTION 2: Add Exam ───────
st.subheader("📅 "+get_text("add_exam",lang))
with st.form("exam_form"):
    col1,col2 = st.columns(2)
    with col1:
        course_list = [c["name"] for c in data["courses"]]
        if course_list:
            exam_course = st.selectbox(get_text("select_course",lang),course_list)
        else:
            exam_course = st.selectbox(get_text("select_course",lang),[get_text("no_courses",lang)])
    with col2:
        exam_date = st.date_input(get_text("exam_date",lang))
    submitted_exam = st.form_submit_button(get_text("add_exam",lang),use_container_width=True)

    if submitted_exam and course_list:
        if exam_course == get_text('no_courses', lang):
            st.error("⚠️ " + ("Please add courses first!" if lang == 'en' else "يرجى إضافة المواد أولاً!"))
        elif any(e['course'] == exam_course for e in data["exams"]):
            st.warning(f"⚠️ Exam for {exam_course} " + ("already set!" if lang == 'en' else "محدد مسبقاً!"))
        else:
            data["exams"].append({
                "course": exam_course,
                "date": str(exam_date)
            })
            save_data(data)
            st.success(get_text('exam_set', lang).format(exam_course))
            st.rerun()
st.divider()
# 9. Display Tasks
st.subheader(get_text("current_setup",lang))

if not data["courses"] and not data["exams"]:
    st.info(get_text('no_courses', lang))
else:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**{get_text('courses', lang)}**")
        if data["courses"]:
            for c in data["courses"]:
                st.markdown(f"🔹 **{c['name']}** — {c['hours']}h/week")
        else:
            st.caption(get_text('no_courses', lang))
    
    with col2:
        st.markdown(f"**{get_text('exams', lang)}**")
        if data["exams"]:
            for e in data["exams"]:
                st.markdown(f"📅 **{e['course']}**: {e['date']}")
        else:
            st.caption(get_text('no_exams', lang))

#10 ─────── Reset Button ───────
st.divider()
if st.button(get_text('reset_data', lang), type="secondary", use_container_width=True):
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
        st.success("✅ " + ("All data reset!" if lang == 'en' else "تم إعادة تعيين جميع البيانات!"))
        st.rerun()

# ─────────────────────────────────────────────────────────────
# 11. CUSTOM FOOTER
# ─────────────────────────────────────────────────────────────
add_footer("📚 " + ("Setup Page" if lang == 'en' else "صفحة الإعداد") + " • Wateera")