from datetime import datetime
import csv

def main():
    check_file()
    while True:
        print("""
-=-=-=-=-=-=To-do list=-=-=-=-=-=-
1. Add Task
2. Show Tasks
3. Mark Tasks as Done
4. Reset the List
5. Exit
    """)

        choice = int(input("select an option: "))

        if choice == 1:
            quantity = int(input("How many tasks do you want to add? "))
            for i in range(quantity):
                number = i + 1
                if number == 1:
                    ordinal = "st"
                elif number == 2:
                    ordinal = "nd"
                elif number == 3:
                    ordinal = "rd"
                else:
                    ordinal= "th"

                task = str(input(f"Insert the {i + 1}{ordinal} task: ")).capitalize()
                task_date = str(input("Insert the Task Date(YYYY-MM-DD): "))
                task_time = str(input("Insert the Task Time(HH:MM AM): "))

                add_task(task, task_date, task_time)

        elif choice == 2:
            task_list = show_tasks()
            index = 0
            for i in range(len(task_list)):
                task_key = task_list[index]["task"]
                date_key = task_list[index]["date"]
                time_key = task_list[index]["time"]
                status_key = task_list[index]["status"]
                index += 1
                task_date, current_date = get_date(date_key, time_key)
                if status_key == "DONE":
                    print(f"\033[32m{task_key:<5} {time_key} ✔\033[m")

                else:
                    if task_date < current_date:
                        result = f"\033[31m{time_key}\033[m"
                    elif task_date > current_date:
                        result = f"\033[32m{time_key}\033[m"

                    print(f"{task_key:<5} {result}")

        elif choice == 3:
            task_list = show_tasks()
            index = 0
            for i in range(len(task_list)):
                task_key = task_list[index]["task"]
                date_key = task_list[index]["date"]
                time_key = task_list[index]["time"]
                status_key = task_list[index]["status"]
                index += 1
                task_date, current_date = get_date(date_key, time_key)
                if status_key == "DONE":
                    print(f"\033[32m{task_key:<5} {time_key} ✔\033[m")

                else:
                    if task_date < current_date:
                        result = f"\033[31m{time_key}\033[m"
                    elif task_date > current_date:
                        result = f"\033[32m{time_key}\033[m"

                    print(f"{task_key:<5} {result}")
            edit_task()
            # task_done = str(input("Which task do you want mark as DONE? "))

        elif choice == 4:
            with open("task_list.txt", "w", newline="") as task_file:
                fieldnames = ["task","date","time","status"]
                writer = csv.DictWriter(task_file, fieldnames=fieldnames)
                writer.writeheader()

        elif choice == 5:
            break

def check_file():
    try:
        with open("task_list.txt", "r") as task_file:
            has_data = task_file.readline().strip() != ""
    except FileNotFoundError:
        has_data = False
    
    with open("task_list.txt", "at", newline="") as task_file:
        fieldnames = ["task","date","time","status"]
        writer = csv.DictWriter(task_file, fieldnames=fieldnames)
        if not has_data:
            writer.writeheader()

def add_task(task, date, time):
    with open("task_list.txt", "at") as task_file:
        task_file.write(f"{task},{date},{time},\n")

def show_tasks():
    task_dict = []
    with open("task_list.txt", "r") as task_file:
        reader = csv.DictReader(task_file)
        for line in reader:
                task_dict.append(line)
    return task_dict

def get_date(date, time):
    task_date = datetime.strptime(f"{date} {time}", "%Y-%m-%d %I:%M %p")
    current_date = datetime.strptime(f"{datetime.now():%Y-%m-%d %I:%M %p}", "%Y-%m-%d %I:%M %p")
    return task_date, current_date

def edit_task():
    rows = []
    task = str(input("Task's name you DONE: ")).capitalize()

    with open("task_list.txt", "r") as task_file:
        reader = csv.DictReader(task_file)
        for line in reader:
            if line["task"] == task:
                line["status"] = "DONE"
            rows.append(line)

    with open("task_list.txt", "w", newline="") as task_file:
        fieldnames = ["task", "date", "time", "status"]
        writer = csv.DictWriter(task_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()

