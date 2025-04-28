import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a new task
def add_task(task_text):
    if task_text:
        st.session_state.tasks.append({
            'id': len(st.session_state.tasks) + 1,
            'text': task_text,
            'completed': False
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
def edit_task(task_id, new_text):
    for task in st.session_state.tasks:
        if task['id'] == task_id:
            task['text'] = new_text
            break

# Streamlit app layout
st.title("Task Manager")

# Input for adding a new task
new_task = st.text_input("Add a new task:", "")
if st.button("Add Task"):
    add_task(new_task)
    st.rerun()

# Display tasks
if st.session_state.tasks:
    for task in st.session_state.tasks:
        col1, col2, col3, col4 = st.columns([1, 3, 1, 1])
        
        # Checkbox for task completion
        with col1:
            completed = st.checkbox("", task['completed'], key=f"check_{task['id']}")
            if completed != task['completed']:
                toggle_task(task['id'])
                st.rerun()
        
        # Task text
        with col2:
            if f"edit_{task['id']}" in st.session_state and st.session_state[f"edit_{task['id']}"]:
                new_text = st.text_input("Edit task:", task['text'], key=f"edit_input_{task['id']}")
                if st.button("Save", key=f"save_{task['id']}"):
                    edit_task(task['id'], new_text)
                    st.session_state[f"edit_{task['id']}"] = False
                    st.rerun()
            else:
                st.write(task['text'], unsafe_allow_html=True)
                if task['completed']:
                    st.markdown("<s>{}</s>".format(task['text']), unsafe_allow_html=True)
                else:
                    st.write(task['text'])
        
        # Edit button
        with col3:
            if st.button("Edit", key=f"edit_btn_{task['id']}"):
                st.session_state[f"edit_{task['id']}"] = True
                st.rerun()
        
        # Delete button
        with col4:
            if st.button("Delete", key=f"delete_{task['id']}"):
                delete_task(task['id'])
                st.rerun()
else:
    st.write("No tasks yet. Add a task above!")

# Note about session persistence
st.write("*Note:* Tasks are stored in the session state and will reset when the app is closed.")