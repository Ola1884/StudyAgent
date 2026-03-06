import streamlit as st

st.set_page_config(page_title="AI Study Planner", page_icon="🎓")

st.title("_وتيرة_ :bar_chart:",width="stretch",text_alignment="right")
st.write("ابدأ تنتهي")
st.write("خطط اجتهد تصل")

st.page_link("pages/Tasks.py", label="Add Tasks", icon="📝")
st.page_link("pages/Plan.py", label="View & Generate Plan", icon="🗓️")
if st.button(label="Tasks",on_click="pages/Tasks.py"):
    st.switch_page("pages/Tasks.py", label="Add Tasks", icon="📝")
with st.sidebar:
    st.image("", width=50)
    st.title("Menu")