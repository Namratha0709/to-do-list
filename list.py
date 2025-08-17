def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save & Exit")
    print("===========================\n")

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()
    print("Welcome to your To-Do List ✅")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if not tasks:
                print("No tasks yet! 🎉")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Task '{task}' added ✅")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Enter task number to remove: "))
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' removed ❌")
                except (ValueError, IndexError):
                    print("Invalid choice, try again!")

        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved! Goodbye 👋")
            break

        else:
            print("Invalid option! Please choose 1-4.")

if __name__ == "__main__":
    main()
