import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="AI Planner", page_icon="🗓️", layout="wide")

# 2. Initialize Session State (This saves data temporarily)
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# 3. Sidebar for Settings
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("Manage your daily focus")
    # You can add more settings later (like work hours)
    st.info("Day 1: Basic Setup")

# 4. Main Interface
st.title("🗓️ AI Planner")
st.write("Add your tasks below, and let's organize them!")

# 5. Input Form
with st.form("task_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        task_name = st.text_input("Task Name", placeholder="e.g., Study Math")
    with col2:
        hours = st.number_input("Hours Needed", min_value=0.5, max_value=12.0, step=0.5)
    with col3:
        priority = st.selectbox("Priority", ["High 🔴", "Medium 🟡", "Low 🟢"])
    
    submitted = st.form_submit_button("Add Task")

# 6. Logic to Save Task
if submitted and task_name:
    new_task = {
        "name": task_name,
        "hours": hours,
        "priority": priority
    }
    st.session_state.tasks.append(new_task)
    st.success(f"✅ Added: {task_name}")

# 7. Display Tasks
st.divider()
st.subheader("📋 Your Task List")

if len(st.session_state.tasks) == 0:
    st.write("No tasks yet. Add one above!")
else:
    for i, task in enumerate(st.session_state.tasks, 1):
        # Display each task in a nice box
        with st.container():
            c1, c2, c3 = st.columns([3, 1, 1])
            c1.write(f"**{i}. {task['name']}**")
            c2.write(f"⏳ {task['hours']} hrs")
            c3.write(f"{task['priority']}")
            st.divider()