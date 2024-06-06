# Priority: Sort by task priority in the order of Urgent > High > Medium > Low.
# Start Date and Time: For tasks with the same priority, sort by the start date and time.

import json
from datetime import datetime

# Sample JSON data
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
                    "task_duration": "02 minutes"
                },
                {
                    "task_template_assignment_id": 2,
                    "task_priority_name": "Low",
                    "task_start_datetime": "25 Apr, 2024",
                    "task_duration": "Flexible"
                },
                {
                    "task_template_assignment_id": 3,
                    "task_priority_name": "High",
                    "task_start_datetime": "25 Apr, 2024 4:22 PM",
                    "task_duration": "01 hours"
                },
                {
                    "task_template_assignment_id": 4,
                    "task_priority_name": "Medium",
                    "task_start_datetime": "25 Apr, 2024 2:22 PM",
                    "task_duration": "01 hours"
                }
            ]
        }
    ]
}
'''

# Load JSON data
tasks_data = json.loads(data)

# Priority order mapping
priority_order = {
    "Urgent": 1,
    "High": 2,
    "Medium": 3,
    "Low": 4
}

# Function to parse date strings into datetime objects
def parse_datetime(datetime_str):
    try:
        return datetime.strptime(datetime_str, "%d %b, %Y %I:%M %p")
    except ValueError:
        return datetime.strptime(datetime_str, "%d %b, %Y")

# Function to sort tasks by priority and start datetime
def sort_tasks(tasks_data):
    for employee in tasks_data["my_tasks"]:
        tasks = employee["tasks"]
        tasks.sort(key=lambda task: (
            priority_order[task["task_priority_name"]],
            parse_datetime(task["task_start_datetime"])
        ))
    return tasks_data

# Sort tasks
sorted_tasks_data = sort_tasks(tasks_data)

# Print sorted tasks for each employee
for employee in sorted_tasks_data["my_tasks"]:
    print(f"Tasks for {employee['employee_name']}:")
    for task in employee["tasks"]:
        print(f"  Task ID: {task['task_template_assignment_id']}, Priority: {task['task_priority_name']}, Start: {task['task_start_datetime']}, Duration: {task['task_duration']}")

# Output:
# Tasks for Sachin R Satam:
#   Task ID: 1, Priority: Urgent, Start: 25 Apr, 2024 3:20 PM, Duration: 02 minutes
#   Task ID: 3, Priority: High, Start: 25 Apr, 2024 4:22 PM, Duration: 01 hours
#   Task ID: 4, Priority: Medium, Start: 25 Apr, 2024 2:22 PM, Duration: 01 hours
#   Task ID: 2, Priority: Low, Start: 25 Apr, 2024, Duration: Flexible