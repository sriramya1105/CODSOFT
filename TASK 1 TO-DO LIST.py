from datetime import datetime

def add_task(tasks):
    task_description = input("Enter the new task: ")
    due_date_str = input("Enter due date (YYYY-MM-DD HH:MM) or leave empty: ")
    due_date = None
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Task will not have a due date.")
    task = {
        'description': task_description,
        'status': 'Pending',
        'due_date': due_date
    }
    tasks.append(task)
    print(f"Task '{task_description}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        due_date = task['due_date'].strftime("%Y-%m-%d %H:%M") if task['due_date'] else "No due date"
        print(f"{idx}. {task['description']} - {task['status']} - Due: {due_date}")
    print("")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]['status'] = 'Completed'
            print(f"Task '{tasks[task_num - 1]['description']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['description']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def edit_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to edit: "))
        if 0 < task_num <= len(tasks):
            task = tasks[task_num - 1]
            new_description = input(f"Enter new task description (leave blank to keep '{task['description']}'): ")
            new_status = input(f"Enter new status (leave blank to keep '{task['status']}'): ")
            new_due_date_str = input(f"Enter new due date (YYYY-MM-DD HH:MM) (leave blank to keep existing): ")

            if new_description:
                task['description'] = new_description
            if new_status:
                task['status'] = new_status
            if new_due_date_str:
                try:
                    task['due_date'] = datetime.strptime(new_due_date_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    print("Invalid date format. Keeping the existing due date.")
            print(f"Task '{task['description']}' updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Edit Task")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            edit_task(tasks)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()