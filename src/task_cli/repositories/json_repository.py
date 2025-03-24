"""
JSON Repository module

Handles persistence and retrieval of Task entities using JSON files.
"""

import json
from typing import List, Dict
import pandas as pd
from task_cli.entities.task import Task


class JSONRepository:
    """JSON Repository class"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def load_json_file(self) -> List[Task]:
        """Load task JSON file"""
        try:
            with open(self.file_name, "r", encoding="utf-8") as data_file:
                tasks = json.load(data_file)
                return [Task.from_dict(task) for task in tasks]
        except FileNotFoundError:
            return []

    def save_json_file(self, task_list: List[Task]) -> None:
        """save dictionary list as JSON file"""
        task_dict = [task.to_dict() for task in task_list]
        with open(self.file_name, "w", encoding="utf-8") as data_file:
            json.dump(task_dict, data_file, indent=2)

    def show_data(self, dict_list: List[Dict[str, str]]) -> pd.DataFrame:
        """Return Json as dataframe"""
        df = pd.DataFrame.from_dict(dict_list)
        return df
