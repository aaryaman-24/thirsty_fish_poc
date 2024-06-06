# Calculate the total work done by each employee by summing the durations of their completed tasks.
# Count the number of pending tasks for each employee.
# Select the employee with the least work done. If theres a tie, select the one with the least pending tasks.

import json
from datetime import timedelta

# Sample JSON data with 4 employees
data = '''
{
    "my_tasks": [
        {
            "employee_id": 1,
            "employee_code": "EMP-A5-00001",
            "employee_name": "Sachin R Satam",
            "employee_picture": "https://i.ibb.co/yhH8LXd/user.png",
            "tasks": [
                {
                    "task_template_assignment_id": 1,
                    "task_priority_name": "Urgent",
                    "task_start_datetime": "25 Apr, 2024 3:20 PM",
                    "task_duration": "02 minutes",
                    "task_employee_status": "completed"
                },
                {
                    "task_template_assignment_id": 2,
                    "task_priority_name": "Low",
                    "task_start_datetime": "25 Apr, 2024",
                    "task_duration": "Flexible",
                    "task_employee_status": "ongoing"
                }
            ]
        },
        {
            "employee_id": 2,
            "employee_code": "EMP-A5-00002",
            "employee_name": "Saliem A Shaikh",
            "employee_picture": "https://i.ibb.co/yhH8LXd/user.png",
            "tasks": [
                {
                    "task_template_assignment_id": 3,
                    "task_priority_name": "High",
                    "task_start_datetime": "25 Apr, 2024 4:22 PM",
                    "task_duration": "01 hours",
                    "task_employee_status": "completed"
                },
                {
                    "task_template_assignment_id": 4,
                    "task_priority_name": "Medium",
                    "task_start_datetime": "25 Apr, 2024 2:22 PM",
                    "task_duration": "01 hours",
                    "task_employee_status": "ongoing"
                }
            ]
        },
        {
            "employee_id": 3,
            "employee_code": "EMP-A5-00003",
            "employee_name": "Kamlesh A Prajapat",
            "employee_picture": "https://i.ibb.co/yhH8LXd/user.png",
            "tasks": [
                {
                    "task_template_assignment_id": 5,
                    "task_priority_name": "Medium",
                    "task_start_datetime": "22 Apr, 2024",
                    "task_duration": "Flexible",
                    "task_employee_status": "completed"
                },
                {
                    "task_template_assignment_id": 6,
                    "task_priority_name": "High",
                    "task_start_datetime": "22 Apr, 2024 5:05 PM",
                    "task_duration": "01 minutes",
                    "task_employee_status": "completed"
                }
            ]
        },
        {
            "employee_id": 4,
            "employee_code": "EMP-A5-00004",
            "employee_name": "Deepak A Gupta",
            "employee_picture": "https://i.ibb.co/yhH8LXd/user.png",
            "tasks": [
                {
                    "task_template_assignment_id": 7,
                    "task_priority_name": "High",
                    "task_start_datetime": "22 Apr, 2024 6:23 PM",
                    "task_duration": "03 hours",
                    "task_employee_status": "completed"
                },
                {
                    "task_template_assignment_id": 8,
                    "task_priority_name": "Urgent",
                    "task_start_datetime": "22 Apr, 2024 2:54 PM",
                    "task_duration": "02 hours",
                    "task_employee_status": "ongoing"
                }
            ]
        }
    ]
}
'''

# Load JSON data
tasks_data = json.loads(data)

# Helper function to parse duration strings into timedelta objects
def parse_duration(duration_str):
    if duration_str.lower() == "flexible":
        return timedelta(0)
    parts = duration_str.split(", ")
    duration = timedelta()
    for part in parts:
        num, unit = part.split()
        if unit.startswith('minute'):
            duration += timedelta(minutes=int(num))
        elif unit.startswith('second'):
            duration += timedelta(seconds=int(num))
        elif unit.startswith('hour'):
            duration += timedelta(hours=int(num))
        elif unit.startswith('day'):
            duration += timedelta(days=int(num))
    return duration

# Function to calculate total work done and count pending tasks
def calculate_work_and_pending(tasks_data):
    employee_stats = {}
    for employee in tasks_data["my_tasks"]:
        total_work = timedelta(0)
        pending_tasks = 0
        for task in employee["tasks"]:
            if task["task_employee_status"] == "completed":
                total_work += parse_duration(task["task_duration"])
            else:
                pending_tasks += 1
        employee_stats[employee["employee_id"]] = {
            "employee_name": employee["employee_name"],
            "total_work": total_work,
            "pending_tasks": pending_tasks
        }
    return employee_stats

# Function to find the employee with the least work done and least pending tasks
def find_least_work_employee(tasks_data):
    employee_stats = calculate_work_and_pending(tasks_data)
    least_work_employee = min(employee_stats.items(), key=lambda x: (x[1]["total_work"], x[1]["pending_tasks"]))
    return least_work_employee[1]["employee_name"]

# Find and print the employee with the least work done and least pending tasks
least_work_employee_name = find_least_work_employee(tasks_data)
print(f"The employee with the least work done and least pending tasks is: {least_work_employee_name}")
