import streamlit as st

st.set_page_config(page_title="AI Study Planner", page_icon="🎓")

st.title("🎓 AI Study Planner")
st.write("Welcome! Please set up your courses first.")

st.page_link("pages/Tasks.py", label="Add Tasks", icon="📝")
#st.page_link("pages/2_🗓️_My_Plan.py", label="🗓️ View & Generate Plan", icon="🗓️")