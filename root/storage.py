import os
import json
from .user import User
from .project import Project
from .task import Task

# Define folder and files
DATA_FOLDER = "../data"
FILE = os.path.join(DATA_FOLDER, "data.json")

# Ensure folder exists
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

def save_info(users):
   # Save all users
    data = [user.to_dict() for user in users]
    for user in users:
        user_dict = {
            "username": user.username,
            "email": user.email,
            "projects": []
        }
        for project in user.projects:
            project_dict = {
                "name": project.name,
                "description": project.description,
                "tasks": []
            }
            for task in project.tasks:
                task_dict = {
                    "title": task.title,
                    "description": task.description,
                    "priority": task.priority,
                    "completed": task.completed
                }
                project_dict["tasks"].append(task_dict)
            user_dict["projects"].append(project_dict)
        data.append(user_dict)

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