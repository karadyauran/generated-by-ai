# models/task.py

import uuid

class Task:
    """
    Task model to represent a task with unique ID, name, due date, and priority.
    """

    def __init__(self, name, due_date, priority, id=None):
        """
        Initialize a new task instance.

        Parameters:
        name (str): The name of the task.
        due_date (str): The due date for the task.
        priority (str): The priority level of the task.
        id (str): Unique identifier for the task (optional).
        """
        self.id = id or str(uuid.uuid4())  # Assign a unique ID if none is provided
        self.name = name
        self.due_date = due_date
        self.priority = priority

    def to_dict(self):
        """
        Converts the Task object into a dictionary.

        Returns:
        dict: The task's attributes in dictionary form.
        """
        return {
            'id': self.id,
            'name': self.name,
            'due_date': self.due_date,
            'priority': self.priority
        }

    def __str__(self):
        """
        String representation of the Task object.

        Returns:
        str: Formatted string displaying task details.
        """
        return f"Task ID: {self.id} | Name: {self.name} | Due: {self.due_date} | Priority: {self.priority}"

    def __eq__(self, other):
        """
        Checks equality based on task ID.

        Parameters:
        other (Task): The other task object to compare.

        Returns:
        bool: True if IDs are equal, False otherwise.
        """
        if isinstance(other, Task):
            return self.id == other.id
        return False
