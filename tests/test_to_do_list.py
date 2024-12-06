import pytest
from lib.to_do_list import *

def test_adding_tasks():
    task = "Pick up drycleaning"
    note = "cleaners closes at 5pm"
    todolist = ToDoList()
    result = todolist.adding_task(task, note)
    assert result == [{"task":"Pick up drycleaning","note":"cleaners closes at 5pm","status":False}]

    task = "Take Molly for a walk"
    note = "Her leash is the green one"
    result = todolist.adding_task(task, note)
    assert result == [{"task":"Pick up drycleaning","note":"cleaners closes at 5pm","status":False}, {"task":"Take Molly for a walk","note":"Her leash is the green one","status":False}]

def test_no_task():
    task = None
    note = "In the attic"
    todolist = ToDoList()
    with pytest.raises(Exception) as e:
        todolist.adding_task(task, note)
    error_message = str(e.value)
    assert error_message == "A task and a note must be added"
    

def test_completing_an_item():
    task = "Pick up drycleaning"
    note = "cleaners closes at 5pm"
    todolist = ToDoList()
    todolist.adding_task(task, note)
    result = todolist.complete_task(task)
    assert result == [{"task":"Pick up drycleaning","note":"cleaners closes at 5pm","status":True}]

def test_show_completed_tasks():
    task = "Pick up drycleaning"
    note = "cleaners closes at 5pm"
    todolist = ToDoList()
    todolist.adding_task(task, note)
    todolist.complete_task(task)
    result = todolist.show_completed_tasks() 
    assert result == [{"task":"Pick up drycleaning", "note":"cleaners closes at 5pm", "status":True}]

def test_show_multiple_completed_tasks():
    task = "Pick up drycleaning"
    note = "cleaners closes at 5pm"
    todolist = ToDoList()
    todolist.adding_task(task,note)
    todolist.complete_task(task)
    task = "Take Molly for a walk"
    note = "Her leash is the green one"
    todolist.adding_task(task,note)
    todolist.complete_task(task)
    result = todolist.show_completed_tasks()
    assert result == [{"task":"Pick up drycleaning","note":"cleaners closes at 5pm","status":True}, {"task":"Take Molly for a walk","note":"Her leash is the green one","status":True}]
    
def test_show_multiple_incomplete_tasks():
    task = "Pick up drycleaning"
    note = "cleaners closes at 5pm"
    todolist = ToDoList()
    todolist.adding_task(task,note)
    task = "Take Molly for a walk"
    note = "Her leash is the green one"
    todolist.adding_task(task,note)
    result = todolist.show_incomplete_tasks()
    assert result == [{"task":"Pick up drycleaning","note":"cleaners closes at 5pm","status":False}, {"task":"Take Molly for a walk","note":"Her leash is the green one","status":False}]
    
