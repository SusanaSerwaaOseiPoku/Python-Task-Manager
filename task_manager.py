## Create your task
## Delete your task
## Mark task as complete

##View your tasks
##

tasks = []

def add_task():
    global tasks
    task_name = input("Enter a task: ")
    tasks.append({"task": task_name, "completed": False})
    print("Task added successfully.")

def delete_task():
    global tasks
    task_name = input("Enter the task you want to delete: ")
    for t in tasks:
        if t["task"] == task_name:
            tasks.remove(t)
            print("Task deleted successfully.")
            return
    print("Task not found.")

def mark_task_as_complete():
    global tasks
    task_name = input("Enter the task you want to mark as complete: ")
    for t in tasks:
        if t["task"] == task_name:
            t["completed"] = True
            print("Task marked as complete.")
            return
    print("Task not found.")

def view_task():
    global tasks
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "✔️" if t["completed"] else "❌"
        print(f"{status} {t['task']}")

def exit_program():
    print("Exiting the task manager.")
    exit()

def main():
    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Complete")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            mark_task_as_complete()
        elif choice == "4":
            view_task()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()