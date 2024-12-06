class ToDoList:
    def __init__(self):
        self.todolist = []
    
    def adding_task(self, task, note):
        if type(task) is str and type(note) is str:
            for job in self.todolist:
                if job["task"] == task and job["status"] == False:
                    return f"Task {task} already exists and is not yet completed."       
            self.todolist.append({"task":task, "note":note,"status":False})
            return self.todolist
        else:
            raise Exception("A task and a note must be added")

    def complete_task(self, task):
        for job in self.todolist:
            if job["task"] == task and job["status"] == False:
                job["status"] = True
        return self.todolist
    
    def show_completed_tasks(self):
        completed_tasks = []    
        for job in self.todolist:
            if job["status"] == True:
                completed_tasks.append(job)
        return completed_tasks

    def show_incomplete_tasks(self):
        incomplete_tasks = []    
        for job in self.todolist:
            if job["status"] == False:
                incomplete_tasks.append(job)
        return incomplete_tasks