class Task:
    def __init__(self, title, description="", priority=1):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        return f"Task(title='{self.title}', completed={self.completed})"

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }