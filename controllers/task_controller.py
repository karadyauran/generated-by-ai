# controllers/task_controller.py

from services.task_manager import TaskManager

class TaskController:
    """
    Controller layer to handle user interaction logic for managing tasks.
    Calls upon TaskManager to perform operations.
    """

    def __init__(self):
        """
        Initializes TaskController with a TaskManager instance.
        """
        self.task_manager = TaskManager()

    def display_tasks(self):
        """
        Displays all current tasks to the console.
        """
        tasks = self.task_manager.get_tasks()
        for task in tasks:
            print(task)

    def add_task(self, name, due_date, priority):
        """
        Adds a new task by delegating to the task manager.

        Parameters:
        name (str): The name of the task.
        due_date (str): The due date for the task.
        priority (str): The priority level of the task.
        """
        self.task_manager.add_task(name, due_date, priority)

    def remove_task(self, task_id):
        """
        Removes a task based on its ID via the task manager.

        Parameters:
        task_id (str): The unique ID of the task to be removed.
        """
        self.task_manager.remove_task(task_id)

    def update_task_status(self, task_id, new_status):
        """
        Updates the status of a task via the task manager.

        Parameters:
        task_id (str): The unique ID of the task to update.
        new_status (str): The new status to apply to the task.
        """
        for task in self.task_manager.get_tasks():
            if task.id == task_id:
                task.status = new_status
                self.task_manager.save_tasks()
                break
