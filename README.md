Task Manager Web App (Streamlit)
A simple Task Manager web application built with Streamlit in Python. Users can add, edit, delete, and mark tasks as complete, with data persisted in the session state during the app's runtime.
Features

Add new tasks
Edit existing tasks
Delete tasks
Mark tasks as complete/incomplete (with strikethrough for completed tasks)
Responsive design via Streamlit
Session state persistence (tasks persist during the session)

Tech Stack

Python: Core programming language
Streamlit: Framework for building the web app

Getting Started
Prerequisites

Python 3.7 or higher
Streamlit (pip install streamlit)

Installation

Clone the repository:git clone https://github.com/your-username/task-manager.git


Navigate to the project directory:cd task-manager


Install the required dependencies:pip install streamlit


Run the app:streamlit run task_manager.py

Streamlit will automatically open the app in your default browser at http://localhost:8501.

Usage

Add a Task: Enter a task in the input field and click "Add Task".
Edit a Task: Click the "Edit" button next to a task, modify the text, and click "Save".
Delete a Task: Click the "Delete" button next to a task.
Complete a Task: Check the checkbox to mark a task as complete (strikes through the text).
Note: Tasks are stored in the session state and will reset when the app session ends.

Project Structure
task-manager/
├── task_manager.py  # Main application file
└── README.md       # Project documentation

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.


Acknowledgements

Streamlit
Python

