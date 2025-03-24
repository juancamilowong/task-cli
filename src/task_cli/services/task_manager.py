"""
Task Service Module.

Contains the business logic for managing Task entities.
Handles creation and listing of tasks using the repository.
"""

import datetime
from collections import defaultdict
from typing import List, Dict
from IPython.display import display
from task_cli.entities.task import Task
from task_cli.repositories.json_repository import JSONRepository


DATA_FILE = "task_list.json"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
VALID_ID_MESSAGE = "Please, use a valid ID"


class TaskManager:
    """Task manager class"""

    def __init__(self, repository: JSONRepository):
        self.repository = repository

    def next_id(self, list_dict: List[Dict[str, str]]) -> int:
        """Get the next id number taking the lastone plus one"""
        res = defaultdict(int)
        for task in list_dict:
            res["id"] = max(res["id"], task["id"])

        return int(res["id"]) + 1

    def task_exist(self, _id: int) -> bool:
        """Check if task id exists in JSON file"""
        task_list = self.repository.load_json_file()
        tasks_dict = [task.to_dict() for task in task_list if task.id == int(_id)]
        return bool(len(tasks_dict) > 0)

    def add_task(self, description: str, status: str = "TODO") -> None:
        """Add new task"""
        task_list = self.repository.load_json_file()
        _id = self.next_id([task.to_dict() for task in task_list])
        task_list.append(
            Task(_id, description=description.strip('"'), status=status.strip('"'))
        )
        self.repository.save_json_file(task_list)
        print(f"Task {description} added successfully (ID={_id})")

    def list_tasks(self, status: str) -> List[Dict[str, str]]:
        """List all tasks or filtered by status"""
        task_list = self.repository.load_json_file()
        if bool(status and not status.isspace()):
            return [task.to_dict() for task in task_list if task.status == status]
        return [task.to_dict() for task in task_list]

    def delete_task(self, _id: int) -> None:
        """Delete a task by id"""
        if not _id.isnumeric():
            print(VALID_ID_MESSAGE)
            return
        if self.task_exist(_id):
            task_list = [
                task for task in self.repository.load_json_file() if task.id != int(_id)
            ]
            self.repository.save_json_file(task_list)
        else:
            print(f"Task with id {_id} does not exist")

    def update_task(self, _id: int, **kwargs) -> None:
        """Update task status or description"""

        if not _id.isnumeric():
            print(VALID_ID_MESSAGE)
            return

        task_list = self.repository.load_json_file()
        index_list = [
            index for (index, item) in enumerate(task_list) if item.id == int(_id)
        ]
        if len(index_list) > 0:
            index = index_list[0]
            for key, val in kwargs.items():
                if key == "description":
                    task_list[index].description = val
                if key == "status":
                    task_list[index].status = val

            task_list[index].updated_at = datetime.datetime.now()

            self.repository.save_json_file(task_list)
            print(f"Task {_id} updated")
        else:
            print(f"Task with id {_id} does not exist")

    def show_task_table(self, status: str) -> None:
        """Show Json as dataframe"""
        list_tasks = self.list_tasks(status)
        display(self.repository.show_data(list_tasks))
