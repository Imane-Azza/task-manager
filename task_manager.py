import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Define categories and their corresponding colors
CATEGORIES = {
    "Work": "blue",
    "Personal": "green",
    "Urgent": "red",
    "Other": "gray"
}

# Function to add a new task
def add_task(task_text, category):
    if task_text:
        st.session_state.tasks.append({
            'id': len(st.session_state.tasks) + 1,
            'text': task_text,
            'completed': False,
            'category': category
        })

# Function to toggle task completion
def toggle_task(task_id):
    for task in st.session_state.tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break

# Function to delete a task
def delete_task(task_id):
    st.session_state.tasks = [task for task in st.session_state.tasks if task['id'] != task_id]

# Function to edit a task
def edit_task(task_id, new_text, new_category):
    for task in st.session_state.tasks:
        if task['id'] == task_id:
            task['text'] = new_text
            task['category'] = new_category
            break

# Streamlit app layout
st.title("Task Manager")

# Input for adding a new task with category
col1, col2 = st.columns([3, 1])
with col1:
    new_task = st.text_input("Add a new task:", "")
with col2:
    new_category = st.selectbox("Category:", list(CATEGORIES.keys()), key="new_task_category")

if st.button("Add Task"):
    add_task(new_task, new_category)
    st.rerun()

# Filter tasks by category
filter_category = st.selectbox("Filter by Category:", ["All"] + list(CATEGORIES.keys()), key="filter_category")
filtered_tasks = st.session_state.tasks if filter_category == "All" else [
    task for task in st.session_state.tasks if task['category'] == filter_category
]

# Display tasks
if filtered_tasks:
    for task in filtered_tasks:
        col1, col2, col3, col4, col5 = st.columns([1, 1, 3, 1, 1])
        
        # Checkbox for task completion
        with col1:
            completed = st.checkbox("", task['completed'], key=f"check_{task['id']}")
            if completed != task['completed']:
                toggle_task(task['id'])
                st.rerun()
        
        # Category label with color
        with col2:
            st.markdown(
                f"<span style='background-color: {CATEGORIES[task['category']]}; color: white; padding: 2px 6px; border-radius: 4px;'>{task['category']}</span>",
                unsafe_allow_html=True
            )
        
        # Task text
        with col3:
            if f"edit_{task['id']}" in st.session_state and st.session_state[f"edit_{task['id']}"]:
                new_text = st.text_input("Edit task:", task['text'], key=f"edit_input_{task['id']}")
                new_edit_category = st.selectbox(
                    "Edit Category:", 
                    list(CATEGORIES.keys()), 
                    index=list(CATEGORIES.keys()).index(task['category']),
                    key=f"edit_category_{task['id']}"
                )
                if st.button("Save", key=f"save_{task['id']}"):
                    edit_task(task['id'], new_text, new_edit_category)
                    st.session_state[f"edit_{task['id']}"] = False
                    st.rerun()
            else:
                if task['completed']:
                    st.markdown(f"<s>{task['text']}</s>", unsafe_allow_html=True)
                else:
                    st.write(task['text'])
        
        # Edit button
        with col4:
            if st.button("Edit", key=f"edit_btn_{task['id']}"):
                st.session_state[f"edit_{task['id']}"] = True
                st.rerun()
        
        # Delete button
        with col5:
            if st.button("Delete", key=f"delete_{task['id']}"):
                delete_task(task['id'])
                st.rerun()
else:
    st.write("No tasks yet. Add a task above!")

# Note about session persistence
st.write("*Note:* Tasks are stored in the session state and will reset when the app is closed.")