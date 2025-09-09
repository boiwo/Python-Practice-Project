# === practices.py ===
# Practicing Python basics + relationships

# Variables & Data Types
name = "boiwo"         # string
age = 25               # integer
height = 1.75          # float
is_student = True      # boolean

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# Operators
num1, num2 = 10, 3
print("Addition:", num1 + num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)

# Conditionals
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loops
print("\nLooping 1 to 5:")
for i in range(1, 6):
    print(i)

# Functions
def greet(person):
    return f"Hello, {person}!"

print(greet(name))

# One-to-Many: User → Tasks
class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []  # one user has many tasks

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        print(f"Tasks for {self.username}: {self.tasks}")

user1 = User("boiwo")
user1.add_task("Learn Python")
user1.add_task("Build Project")
user1.view_tasks()

# Many-to-Many: Users ↔ Projects
class Project:
    def __init__(self, title):
        self.title = title
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            user.projects.append(self)

class UserWithProjects:
    def __init__(self, username):
        self.username = username
        self.projects = []

    def view_projects(self):
        print(f"Projects for {self.username}: {[p.title for p in self.projects]}")

# Create users & projects
alice = UserWithProjects("Alice")
benard = UserWithProjects("Benard")

proj1 = Project("SchoolApp")
proj2 = Project("Calculator")

# Link users <-> projects
proj1.add_user(alice)
proj1.add_user(benard)
proj2.add_user(benard)

# View results
alice.view_projects()
benard.view_projects()
