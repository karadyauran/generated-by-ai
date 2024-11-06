# main.py

from controllers.task_controller import TaskController


def show_menu():
    """
    Displays the main menu options to the user.
    """
    print("\nMain Menu:")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Update task status")
    print("5. Exit")


def main():
    """
    The main entry point of the application.
    Handles user input and task management.
    """
    controller = TaskController()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            controller.display_tasks()
        elif choice == '2':
            name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (high, medium, low): ")
            controller.add_task(name, due_date, priority)
        elif choice == '3':
            task_id = input("Enter task ID to remove: ")
            controller.remove_task(task_id)
        elif choice == '4':
            task_id = input("Enter task ID to update: ")
            new_status = input("Enter new status (pending, completed): ")
            controller.update_task_status(task_id, new_status)
        elif choice == '5':
            print("Exiting the task manager.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
