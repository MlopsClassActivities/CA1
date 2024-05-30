from tasks import TaskManager

def main():
    task_manager = TaskManager()
    # Basic menu for interaction
    while True:
        print("1. Add Task\n2. List Tasks\n3. Delete Task\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            task = input("Enter task to delete: ")
            task_manager.delete_task(task)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
