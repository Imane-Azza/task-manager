Task Manager Web App (Streamlit)
A simple and efficient Task Manager web application built with Streamlit and Python.
Users can add, edit, delete, and mark tasks as complete, with task categories and color-coded labels for better organization.
All data is persisted within the session state during the app's runtime.

✨ Features
➕ Add new tasks with a category (Work, Personal, Urgent, Other)

✏️ Edit existing tasks and their categories

🗑️ Delete tasks

✅ Mark tasks as complete/incomplete (completed tasks appear with strikethrough)

🏷️ Color-coded category labels for tasks

🔍 Filter tasks by category

📱 Responsive and user-friendly UI with Streamlit

💾 Session state persistence (tasks persist during the active session)

🛠 Tech Stack
Python — Core programming language

Streamlit — Framework for building the web application

🚀 Getting Started
Prerequisites
Python 3.7 or higher

Streamlit (pip install streamlit)

Installation
Clone the repository

bash
Copier
Modifier
git clone https://github.com/Imane-Azza/task-manager.git
Navigate to the project directory

bash
Copier
Modifier
cd task-manager
Install dependencies

bash
Copier
Modifier
pip install streamlit
Run the app

bash
Copier
Modifier
streamlit run task_manager.py
Once started, Streamlit will open the app automatically in your default browser at http://localhost:8501.

📋 Usage
Add a Task: Enter a task description, select a category (Work, Personal, Urgent, Other), and click "Add Task".

Edit a Task: Click "Edit" next to a task, update its text and/or category, and click "Save".

Delete a Task: Click "Delete" next to a task to remove it.

Mark as Complete: Use the checkbox to mark tasks as completed (completed tasks are shown with a strikethrough).

Filter Tasks: Select a category from the dropdown to filter tasks, or view all tasks.

Note:
Tasks are saved only during the current session. Restarting or refreshing the app will reset the tasks.

📁 Project Structure
bash
Copier
Modifier
task-manager/
├── task_manager.py  # Main application file
└── README.md        # Project documentation
🤝 Contributing
We welcome contributions! To contribute:

Fork the repository

Create a new branch

bash
Copier
Modifier
git checkout -b feature/your-feature
Make your changes and commit them

bash
Copier
Modifier
git commit -m "Add your feature"
Push to your branch

bash
Copier
Modifier
git push origin feature/your-feature
Open a Pull Request and describe your changes.


🙏 Acknowledgements
Streamlit

Python