import os
import json
from .user import User
from .project import Project
from .task import Task

# Define folder and files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER =os.path.join(BASE_DIR, "..", "data")
FILE = os.path.join(DATA_FOLDER, "data.json")

# Ensure folder exists
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

def save_info(users):
    data = [user.to_dict() for user in users]

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    
   # Load all users
    users = []
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

    for user_dict in data:
        user = User(user_dict["username"], user_dict["email"])
        for project_dict in user_dict["projects"]:
            project = Project(project_dict["name"], project_dict["description"], user)
            for task_dict in project_dict["tasks"]:
                task = Task(task_dict["title"], task_dict["description"], task_dict["priority"])
                if task_dict["completed"]:
                    task.complete()
                project.tasks.append(task)
            user.projects.append(project)
        users.append(user)

    return users