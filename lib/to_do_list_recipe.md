# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

1. As a user so that I can keep track of my tasks
   I want a program that I can add todo tasks to and see a list of them.

2. As a user so that I can focus on tasks to complete
   I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class ToDoList:
    def __init__(self, name, todolist):
        self.name = name
        self.todolist = todolist


        example_todolist = [{task: pick up dry cleaning, description: go to 33 Makers Street, status: False}, {task: other task, description: other description, status: True}]



    def add_task(self, task):

    def show_completed_tasks(self):

    def show_incomplete_tasks(self):

    def complete_task(self, task):

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
