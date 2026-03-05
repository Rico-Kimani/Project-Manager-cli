from .task import Task

class Project:
    def __init__(self, name, description, user):
        self.name = name
        self.description = description
        self.user = user
        self.tasks = []

    def add_task(self, title, description="", priority=1):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task

    def __repr__(self):
        return f"Project(name='{self.name}')"

    def to_dict(self):
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks]
        }