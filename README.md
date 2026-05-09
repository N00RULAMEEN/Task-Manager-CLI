# Task-Manager-CLI
````md
# Task-Manager-CLI

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=30&pause=1000&color=00FF9C&center=true&vCenter=true&width=900&lines=Task+Manager+CLI;Python+Command-Line+Task+Manager;Manage+Tasks+Directly+from+the+Terminal;JSON-Based+Persistent+Storage;Built+with+Python+and+Pytest" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/CLI-Terminal-success?style=for-the-badge&logo=gnubash" />
  <img src="https://img.shields.io/badge/Testing-Pytest-red?style=for-the-badge&logo=pytest" />
  <img src="https://img.shields.io/badge/Storage-JSON-yellow?style=for-the-badge&logo=json" />
</p>

---

# About The Project

**Task Manager CLI** is a command-line based task management application developed in Python.

The goal of this project is to provide a simple and efficient way to manage daily tasks directly from the terminal. Users can create tasks, delete tasks, mark them as completed, filter pending or completed tasks, and monitor their overall progress.

The application also includes:
-  Priority levels
-  Due dates
-  Overdue task detection
-  Progress tracking
-  Automatic cleanup for old tasks
-  Colored terminal output
-  Persistent JSON storage

All task data is stored inside a `CLI_TODO.json` file, ensuring tasks remain saved even after the program is closed.

---

#  Features
-  Add tasks with title, priority, and due date
-  Delete tasks using unique task IDs
-  Mark tasks as completed
-  Filter pending and completed tasks
-  Track overall completion progress
-  Sort tasks by priority
-  Detect overdue tasks automatically
-  Remove tasks older than 30 days
-  Styled terminal interface using Pyfiglet and Colorama
-  JSON-based persistent storage
-  Input validation and duplicate task prevention

---

#  Technologies Used

<p>
<img src="https://skillicons.dev/icons?i=python,github,vscode,json&perline=8" />
</p>

### Libraries
- `pyfiglet`
- `colorama`
- `pytest`

---

# 📂 Project Structure

```bash
project/
│
├── project.py          # Main application logic
├── test_project.py     # Pytest test cases
├── requirements.txt    # External dependencies
├── README.md           # Project documentation
└── CLI_TODO.json       # Stored task data
````

---

#  How It Works

The application starts by loading saved tasks from the JSON file.

Users interact with a terminal menu that provides options to:

* add tasks
* delete tasks
* mark tasks as done
* filter tasks
* open settings
* check progress

Each task contains:

* unique ID
* title
* priority
* due date
* completion status

Tasks are grouped by creation date internally while maintaining separate due dates for flexibility.

---

#  Testing

The project includes automated tests using **pytest**.

### Tested Features

* Adding tasks
* Deleting tasks
* Marking tasks as completed
* Filtering pending tasks

Run tests using:

```bash
pytest test_project.py
```

---

#  Design Decisions

One important design decision was implementing a **global unique ID system** for tasks. Instead of restarting IDs daily, the program generates IDs globally across all stored tasks. This prevents conflicts when deleting or updating tasks.

Another major decision was separating:

* the **task creation date**
  from
* the **task due date**

This makes the application more realistic and flexible.

I also focused heavily on input validation to avoid:

* empty titles
* invalid priorities
* duplicate tasks
* incorrect date formats
* past due dates

---

# 📈 Future Improvements

Planned future upgrades include:

*  Flask web version
*  Edit task feature
*  Search functionality
*  User authentication
*  Cloud database integration
*  Mobile-friendly interface

---

#  Acknowledgements

Special thanks to everyone who creates open-source tools, documentation, and learning resources that help developers improve and build projects.

---

<p align="center">
  <b>Built with Python • Logic • Persistence • Problem Solving</b>
</p>
```

