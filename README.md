
# Flask To-Do App
-------------------------------------------------------------------
A simple Flask-based To-Do application that demonstrates CRUD (Create, Read, Update, Delete) operations with a user-friendly interface.


## Features
- Create: Add new tasks to your to-do list.
- Read: View all tasks in a structured table format.
- Update: Modify existing tasks, including their title and description.
- Delete: Remove tasks from the to-do list.
The app uses SQLite as its database and Bootstrap 5 for a responsive and modern UI.

## Getting Started
### Prerequisites

Ensure you have Python installed. You can download it from 
[Python offical site](https://www.python.org/)


## Installation

1. Clone the repository:

```bash
  git clone https://github.com/Madhur-Prakash/Todo-List
  cd Todo-List
```

2. Install dependencies

```bash
  pip install -r requirements.txt
```

3. Initialize the database:

```bash
  python
>>> from app import db
>>> db.create_all()
>>> exit()
```
4. Run the app:
```bash
  python app.py
```
5. Open your browser and navigate to:
```bash
  http://127.0.0.1:5000/
```

## File Structure 
```bash
├── app.py             # Main Flask application
├── templates/         # HTML templates
│   ├── index.html     # Main page for viewing and adding tasks
│   └── update.html    # Page for updating tasks
├── requirements.txt   # List of dependencies
└── todo.db            # SQLite database (created automatically)

```
## How to use

1. Add a Task:
- Navigate to the homepage.
- Enter a task title and description, then click "Submit."
2.  View Tasks:
- All tasks are displayed in a table on the homepage.
3. Update a Task:
- Click "Update" next to a task in the table.
- Modify the task details and click "Update."
4. Delete a Task:
- Click "Delete" next to a task to remove it.
## Screenshots

![Screenshot 2024-12-01 002201](https://github.com/user-attachments/assets/673fa332-83c4-40c9-8de6-d5faa93d1a9f)

![Screenshot 2024-12-01 002242](https://github.com/user-attachments/assets/dae9f779-80ea-4e17-9d1b-c0aaf7ab0e96)    
## Acknowledgements

 This project was created to demonstrate how to build a basic CRUD application using Flask.

For any feedback or suggestions, feel free to reach out or open an issue in the repository.

### For deeper understanding of the code visit
[Simplifying CRUD Operations with Flask: A Practical Walkthrough - Medium](https://www.python.org/)
