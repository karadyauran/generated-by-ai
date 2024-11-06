# services/task_manager.py

from models.task import Task
from utils.file_handler import FileHandler

class TaskManager:
    """
    TaskManager provides the business logic for managing tasks.
    It interacts with the task model and handles data persistency.
    """

    def __init__(self, data_file='data/tasks.json'):
        """
        Initializes the TaskManager with a file for storing tasks.

        Parameters:
        data_file (str): Path to the JSON file for task data.
        """
        self.file_handler = FileHandler(data_file)
        self.file_handler.ensure_directory_exists()
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Loads tasks from the storage file.

        Returns:
        list of Task: The list of tasks loaded from file.
        """
        tasks_data = self.file_handler.read_data()
        return [Task(**data) for data in tasks_data]

    def save_tasks(self):
        """
        Saves the current list of tasks to the storage file.
        """
        tasks_data = [task.to_dict() for task in self.tasks]
        self.file_handler.write_data(tasks_data)

    def add_task(self, name, due_date, priority):
        """
        Adds a new task to the task list.

        Parameters:
        name (str): The name of the task.
        due_date (str): The due date for the task.
        priority (str): The priority level of the task.
        """
        new_task = Task(name=name, due_date=due_date, priority=priority)
        self.tasks.append(new_task)
        self.save_tasks()

    def remove_task(self, task_id):
        """
        Removes a task from the task list using its ID.

        Parameters:
        task_id (int): The unique identifier of the task to remove.
        """
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def get_tasks(self):
        """
        Retrieves all tasks.

        Returns:
        list of Task: The list of all tasks.
        """
        return self.tasks
