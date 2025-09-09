🐍 Python Practice Project

This project (practices.py) is a simple Python file where I practice basic programming concepts and data relationships.

📌 Features
✅ Python Basics

Variables & Data Types → strings, integers, floats, booleans

Operators → addition, division, floor division

Conditionals → if/else statements

Loops → for loop (1 to 5)

Functions → reusable functions (greet)

✅ Relationships

One-to-Many

A User can have many tasks

Implemented using a User class with a .tasks list

Many-to-Many

Users can join multiple projects

Projects can have multiple users

Implemented with UserWithProjects and Project classes

🗂️ Project Structure

calculator_project/
│── practices.py   # Main practice script
│── README.md      # Project documentation

▶️ How to Run

Navigate into the project folder:

cd ~/Documents/calculator_project


Run the script:

python practices.py

📝 Example Output

Name: boiwo, Age: 25, Height: 1.75, Student: True
Addition: 13
Division: 3.3333333333333335
Floor Division: 3
You are an adult.

Looping 1 to 5:
1
2
3
4
5
Hello, boiwo
Tasks for boiwo: ['Learn Python', 'Build Project']
Projects for Alice: ['SchoolApp']
Projects for Benard: ['SchoolApp', 'Calculator']

📊 ERD (Entity Relationship Diagram)

User (1) ------ (∞) Task
+---------+          +---------+
|  User   | 1     ∞  |  Task   |
+---------+----------+---------+
| id (PK) |          | id (PK) |
| name    |          | content |
+---------+          | user_id (FK) → User.id
                     +---------+



+---------+         +----------------+         +-----------+
|  User   | 1     ∞ | UserProjects   | ∞     1 |  Project  |
+---------+---------+----------------+---------+-----------+
| id (PK) |         | id (PK)        |         | id (PK)   |
| name    |         | user_id (FK)   |         | title     |
+---------+         | project_id (FK)|         +-----------+
                    +----------------+




Learning Goals

Strengthen Python fundamentals

Understand One-to-Many & Many-to-Many relationships

Practice with small, testable code
