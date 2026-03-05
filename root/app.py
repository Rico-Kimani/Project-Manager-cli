from .storage import load_data, save_info
from .user import User
from .project import Project
from .task import Task
from colorama import Fore, Style


class App:
    def __init__(self):
        self.users = load_data()
        self.current_user = None

    def show_menu(self):
        print("\n Project Manager CLI ")
        print("1. Create User")
        print("2. Login")
        print("3. Create Project")
        print("4. Add Task")
        print("5. View")
        print("6. Complete Task")
        print("0. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choice: ").strip()

            if choice == "1":
                self.create_user()

            elif choice == "2":
                self.login()

            elif choice == "3":
                self.create_project()

            elif choice == "4":
                self.add_task()

            elif choice == "5":
                self.view_data()

            elif choice == "6":
                self.complete_task()

            elif choice == "0":
                save_info(self.users)
                print("Goodbye 👋")
                break

            else:
                print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)

    def create_user(self):
        username = input("Username: ").strip()
        email = input("Email: ").strip()

        for user in self.users:
            if user.username == username:
                print("User already exists")
                return

        self.users.append(User(username, email))
        save_info(self.users)
        print(Fore.GREEN + "User created successfully" + Style.RESET_ALL)

    def login(self):
        username = input("Enter username: ").strip()
        for user in self.users:
            if user.username == username:
                self.current_user = user
                print(f"Logged in as {username}")
                return
        print("User not found")

    def create_project(self):
        if not self.current_user:
            print("Please login first")
            return

        name = input("Project name: ").strip()
        description = input("Description: ").strip()

        project = Project(name, description, self.current_user)
        self.current_user.projects.append(project)
        save_info(self.users)
        print("Project created")

    def add_task(self):
        if not self.current_user:
            print("Please login first")
            return

        if not self.current_user.projects:
            print("No projects found")
            return

        project_name = input("Project name: ").strip()

        for project in self.current_user.projects:
            if project.name == project_name:
                title = input("Task title: ").strip()
                description = input("Task description: ").strip()
                priority = input("Priority (Low/Medium/High): ").strip()

                task = Task(title, description, priority)
                project.tasks.append(task)
                save_info(self.users)
                print("Task added")
                return

        print("Project not found")

    def view_data(self):
        for user in self.users:
            print(f"\nUser: {user.username}")
            for project in user.projects:
                print(f"  Project: {project.name}")
                for i, task in enumerate(project.tasks, start=1):
                    status = "Completed" if task.completed else "pending"
                    print(f"{i}. {task.title} - {status}")

    def complete_task(self):
        if not self.current_user:
            print("Please login first")
            return

        project_name = input("Project name: ").strip()

        for project in self.current_user.projects:
            if project.name == project_name:
                for i, task in enumerate(project.tasks, start=1):
                    print(f"{i}. {task.title}")

                index = int(input("Select task number: ")) - 1
                project.tasks[index].mark_complete()
                save_info(self.users)
                print("Task completed ")
                return

        print("Project not found")