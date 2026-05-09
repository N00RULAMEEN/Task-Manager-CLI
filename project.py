import os
import json
from datetime import datetime ,timedelta
import pyfiglet
from colorama import Fore, init


FileName = "CLI_TODO.json"

#1
def welcome_TODO():
    init(autoreset = True)
    Welcome_message = pyfiglet.figlet_format("Welcome to \nTask Manager CLI")
    print(Fore.GREEN + Welcome_message + Fore.RESET)

#2
def Load_Tasks():
    if not os.path.exists(FileName):
        return{}
    
    try:
        with open(FileName, "r") as C:
            return json.load(C)
    except json.JSONDecodeError:
        return{}


#3
def Save_TO_DO(TaskDaily):
    with open(FileName, "w") as W:
        json.dump(TaskDaily, W, indent=4)

#4 ADD
def Add_TO_DO(TaskDaily, priority, title, due_date):
    today = datetime.now().strftime("%Y-%m-%d")

    if today not in TaskDaily :
        TaskDaily[today] = []
    
    Task_Id = max(
        (t["id"] for day in TaskDaily.values() for t in day),
        default=0
    ) + 1
    
    TaskDaily[today].append({
        "id": Task_Id,
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "done": False
        })
    print("Task added successfully.")

    return TaskDaily

#5
def Del_TO_DO(TaskDaily, Task_Id):
    found = False

    for date in list(TaskDaily.keys()):
        new_list = []
        for t in TaskDaily[date]:
            if t["id"] == Task_Id:
                found = True
            else:
                new_list.append(t)

        if new_list:
            TaskDaily[date] = new_list
        else:
            del TaskDaily[date]

    return TaskDaily, found


#6
def mark_done(TaskDaily, Task_Id):

    for date in TaskDaily:
        for task in TaskDaily[date]:
            if task["id"] == Task_Id:
                task["done"] = True
                return TaskDaily, True

    return TaskDaily, False

#7 Delete after 30 Days
def Clean_30(tasks):
    today = datetime.now()

    New_Tasks = {}
    for date in tasks:
        task_date = datetime.strptime(date, "%Y-%m-%d")
        if today - task_date <= timedelta(days=30):
            New_Tasks[date] = tasks[date]

    return New_Tasks

#8
def View_Tasks(TaskDaily):
    if not TaskDaily:
        print("No Task Found")

        return
    
    for date in sorted(TaskDaily.keys()):
        print(f"\n📅 {date}")
        
        for t in TaskDaily[date]:
            if t["done"]:
                status = Fore.GREEN + "✔"
            else:
                status = Fore.RED + "✘"

            if datetime.strptime(t["due_date"], "%Y-%m-%d").date() < datetime.now().date():
                due = Fore.YELLOW + "(OVERDUE)"
            else:
                due = ""

            if t["priority"] == "High":
                priority = Fore.RED + t["priority"]
            elif t["priority"] == "Medium":
                priority = Fore.YELLOW + t["priority"]
            else:
                priority = Fore.GREEN + t["priority"]
            print(f"{t['id']}. {t['title']} [{priority}] Due: {t['due_date']} {due} {status}")

#9 Sort
def sort_tasks(tasks):
    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    for date in tasks:
        tasks[date].sort(key=lambda x: priority_order.get(x["priority"], 99))

    return tasks

#10 Progress V3ever
def show_progress(tasks):
    total = 0
    done = 0

    for date, task_list in tasks.items():
        total += len(task_list)
        for task in task_list:
            if task["done"] is True:
                done += 1

    if total == 0:
        print("No tasks available.")
        return

    percent = (done / total) * 100
    print(f"\nCompleted: {done}/{total}")
    print(f"Progress: {percent:.2f}%")

# 11Settings 
def settings_menu(tasks):
    while True:
        print("\n--- SETTINGS ---")
        print("1. View History")
        print("2. Delete All Tasks")
        print("3. View Progress")
        print("4. Sort Tasks")
        print("5. Clean Tasks (Older than 30 Days)")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            View_Tasks(tasks)

        elif choice == "2":
            confirm = input("Delete ALL tasks? (yes/no): ")
            if confirm.lower() == "yes":
                if os.path.exists(FileName):
                    os.remove(FileName)
                tasks.clear()
                print("All tasks deleted.")

        elif choice == "3":
            show_progress(tasks)

        elif choice == "4":
            tasks = sort_tasks(tasks)
            Save_TO_DO(tasks)
            print("Tasks sorted by priority.")
    
        elif choice == "5":
            confirm = input("Delete tasks older than 30 days? (yes/no): ")
            if confirm.lower() == "yes":
                tasks = Clean_30(tasks)
                Save_TO_DO(tasks)
                print("Old tasks removed.")

        elif choice == "6":
            break

        else:
            print("Invalid choice")

    return tasks

# 12 filter_task
def filter_tasks(tasks, status):
    filtered = {}

    for date in tasks:
        filtered_list = []
        for t in tasks[date]:
            if status == "done" and t["done"]:
                filtered_list.append(t)
            elif status == "pending" and not t["done"]:
                filtered_list.append(t)

        if filtered_list:
            filtered[date] = filtered_list

    return filtered

#13 exit message
def exit_message():
    exit_text = pyfiglet.figlet_format("Thank you for using Task Manager CLI")
    print(Fore.GREEN + exit_text + Fore.RESET)





def main():
    init(autoreset=True)
    tasks = Load_Tasks()   
    welcome_TODO()


    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Done")
        print("4. Show All Tasks")
        print("5. Show Pending")
        print("6. Show Completed")
        print("7. Settings")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            
            if not title.strip():
                 print("Title cannot be empty.")
                 continue
            elif len(title.strip()) < 3:
                 print("Title must be at least 3 characters.")
                 continue

            priority = input("Priority (High/Medium/Low): ")
            #check priority
            priority = priority.strip().capitalize()
            
            if priority not in ["High", "Medium", "Low"]:
                 print("Invalid priority.")
                 continue

            due_date = input("Due Date (YYYY-MM-DD): ")
            #check date
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            if datetime.strptime(due_date, "%Y-%m-%d").date() < datetime.now().date():
                print("Due date cannot be in the past.")
                continue

            tasks = Add_TO_DO(tasks, priority, title, due_date)
            Save_TO_DO(tasks)

        elif choice == "2":
            try:
                task_id = int(input("Task ID: "))
            except ValueError:
                print("Invalid ID")
                continue
            tasks, found = Del_TO_DO(tasks, task_id)
            if not found:
                print("Task ID not found.")
            else:
                print("Task deleted.")
                Save_TO_DO(tasks)

        elif choice == "3":
            try:
                task_id = int(input("Task ID: "))
            except ValueError:
                print("Invalid ID")
                continue
            tasks, found = mark_done(tasks, task_id)
            if found:
                Save_TO_DO(tasks)
                print("Task marked as done.")
            else:
                print("Task ID not found.")

        elif choice == "4":
            View_Tasks(tasks)

        elif choice == "5":
            print("\n--- Pending Tasks ---")
            View_Tasks(filter_tasks(tasks, "pending"))            
        elif choice == "6":
            print("\n--- Completed Tasks ---")
            View_Tasks(filter_tasks(tasks, "done"))

        elif choice == "7":
            tasks = settings_menu(tasks)

        elif choice == "8":
            exit_message()
            break
        
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()