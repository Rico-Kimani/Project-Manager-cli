from .task import Task

class Project:
    def __init__(self, name, description, user):
        self.name = name
        self.description = description
        self.user = user
        self.tasks = []

    def __repr__(self):
        return f"Project(name='{self.name}')"

    def to_dict(self):
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks]
        }