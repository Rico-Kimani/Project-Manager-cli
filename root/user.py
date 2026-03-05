from .project import Project

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.projects = []

    def add_project(self, project_title, description=""):
        project = Project(project_title, description, self)
        self.projects.append(project)
        return project

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects]
        }