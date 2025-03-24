"""
This module help in the JSON tasks management
"""

import json
import datetime
from collections import defaultdict
import pandas as pd




DATA_FILE = "task_list.json"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class Task:
    """Task definition class"""
    #pylint: disable=too-many-arguments, too-many-positional-arguments, redefined-builtin
    def __init__(
        self,
        _id,
        description="",
        status="TODO",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    ):

        self.id = _id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """Return task dictionary"""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.strftime(DATE_FORMAT),
            "updated_at": self.updated_at.strftime(DATE_FORMAT),
        }

    @classmethod
    def from_dict(cls, task_dict):
        """Return task class object"""
        return cls(
            task_dict["id"],
            task_dict["description"],
            task_dict["status"],
            datetime.datetime.strptime(task_dict["created_at"], DATE_FORMAT),
            datetime.datetime.strptime(task_dict["updated_at"], DATE_FORMAT),
        )

    def __str__(self):
        return f"id: {self.id} \
            description: {self.description} \
            status: {self.status} \
            created: {self.created_at} \
            updated: {self.updated_at}"


def load_json_file():
    """Load task JSON file"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as data_file:
            tasks = json.load(data_file)
            return [Task.from_dict(task) for task in tasks]
    except FileNotFoundError:
        return []


def save_task(task_list):
    """save dictionary list as JSON file """
    task_dict = [task.to_dict() for task in task_list]
    with open(DATA_FILE, "w", encoding="utf-8") as data_file:
        json.dump(task_dict, data_file, indent=2)

    show_data(task_dict)


def task_exist(_id):
    """Check if task id exists in JSON file"""
    task_list = load_json_file()
    tasks_dict = [task.to_dict() for task in task_list if task.id == int(_id)]
    return bool(len(tasks_dict) > 0)


def add_task(description, status="TODO"):
    """Ad new task"""
    task_list = load_json_file()
    _id = next_id([task.to_dict() for task in task_list])
    task_list.append(Task(_id, description=description, status=status))
    save_task(task_list)
    print(f"Task {description} added successfully (ID={_id})")


def next_id(list_dict):
    """Get the next id number taking the lastone plus one"""
    res = defaultdict(int)
    for task in list_dict:
        res["id"] = max(res["id"], task["id"])

    return int(res["id"]) + 1


def list_tasks(status):
    """List all tasks or filtered by status"""
    task_list = load_json_file()
    if bool(status and not status.isspace()):
        return [task.to_dict() for task in task_list if task.status == status]
    return [task.to_dict() for task in task_list]


def delete_task(_id):
    """Delete a task by id"""
    task_list = [task for task in load_json_file() if task.id != int(_id)]
    save_task(task_list)


def update_task(_id, **kwargs):
    """Update task status or description"""
    task_list = load_json_file()
    index_list = [index for (index, item) in enumerate(task_list) if item.id == _id]
    if len(index_list) > 0:
        index = index_list[0]
        for key, val in kwargs.items():
            if key == "description":
                task_list[index].description = val
            if key == "status":
                task_list[index].status = val

        task_list[index].updated_at = datetime.datetime.now()

        save_task(task_list)
    else:
        print(f"Task with id {_id} does not exist")


def show_data(data):
    """Show JSON data as table"""
    df = pd.DataFrame.from_dict(data)
    print("\n")
    print(df)
    print("\n")