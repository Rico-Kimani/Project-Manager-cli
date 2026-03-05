Project Manager CLI

Project Manager CLI is a command-line application that simulates a multi-user project tracking system. The application allows users to create accounts, manage projects, add tasks, and track task completion directly from the terminal.

This project demonstrates important Python development concepts such as Object-Oriented Programming (OOP), file handling with JSON, and building interactive CLI applications.

Features

Create user accounts

Login functionality

Create and manage projects

Add tasks to projects

Mark tasks as completed

View projects and their tasks

Persistent data storage using JSON

Simple menu-driven command-line interface

How the Application Works

Users create an account using a username and email.

After logging in, users can create projects.

Each project can contain multiple tasks.

Tasks can be marked as completed.

Users can view all their projects and associated tasks.

All application data is stored locally in a JSON file, ensuring that information persists between sessions.

Example CLI Menu

Example of the menu displayed when running the application:

===== Project Manager CLI =====

1. Create User
2. Login
3. Create Project
4. Add Task
5. View Projects & Tasks
6. Complete Task
7. Exit

Select an option:
----------------------------------------------------------------------------
Project Structure

Your project is organized into modules to separate responsibilities and keep the code maintainable.

Project-Manager
│
├── root
│   ├── app.py
│   ├── manager.py
│   ├── project.py
│   ├── storage.py
│   ├── task.py
│   ├── test.py
│   └── user.py
│
├── main.py
├── README.md
├── Requirement.txt
├── .gitignore
└── LICENSE
Folder / File Explanation

root/
Contains the main modules that implement the application's core logic.

app.py – Main application controller that runs the CLI interface

manager.py – Handles overall system operations and coordination between components

project.py – Defines the Project class and project-related functionality

task.py – Defines the Task class and task management logic

user.py – Defines the User class and user-related operations

storage.py – Handles reading and writing data to the JSON storage file

test.py – Used for testing functionality during development

main.py
The main entry point that starts the application.

Requirement.txt
Lists any external dependencies needed for the project.

README.md
Project documentation.

LICENSE
Defines the license for the project.
---------------------------------------------------------------------------------
Setup Instructions
1 Clone the Repository
git clone https://github.com/Rico-Kimani/Project-Manager-cli

Navigate into the project folder:

cd Project-Manager-cli
2 Install Python

Make sure Python 3 is installed:

python3 --version
3 Run the Application

Start the CLI program by running:

python3 main.py
Using the Application

Use the numbered menu to perform the following actions:

Create a user account

Login

Create projects

Add tasks to projects

View projects and tasks

Mark tasks as completed

Exit the program

All data will automatically be saved locally through the storage system.

Technologies Used

Python 3

JSON for data persistence
--------------------------------------------------------------------------
Learning Objectives

This project was created to practice and demonstrate:

Python Object-Oriented Programming

File handling and JSON storage

Building interactive command-line applications

Organizing a multi-module Python project

Designing a simple project management system

Future Improvements

Possible enhancements for this project include:

Adding task deadlines and priorities

Adding password authentication

Implementing a richer CLI interface using Typer or Click Python CLI Library

Replacing JSON storage with SQLite for more robust data management

Author

Erick Kimani

GitHub:
https://github.com/Rico-Kimani
