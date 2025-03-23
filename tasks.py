import json
import datetime
import pandas as pd
from collections import defaultdict
from collections import namedtuple
from json import JSONEncoder



DATA_FILE = "task_list.json"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

class Task:

    def __init__(self, id, description="", status="TODO", createdAt=datetime.datetime.now(), updatedAt=datetime.datetime.now()):
        
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt	

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'createdAt': self.createdAt.strftime(DATE_FORMAT),
            'updatedAt': self.updatedAt.strftime(DATE_FORMAT)

        }
    
    @classmethod
    def from_dict(cls, task_dict):
        createdAtObj = datetime.datetime.strptime(task_dict['createdAt'], DATE_FORMAT)
        updatedAtObj = datetime.datetime.strptime(task_dict['updatedAt'], DATE_FORMAT)
        return cls(task_dict['id'], task_dict['description'], task_dict['status'], createdAtObj, updatedAtObj)

    def __str__(self):
        return f"id: {self.id} description: {self.description} status: {self.status} created: {self.createdAt} updated: {self.updatedAt}"


def load_tasks():
    try:
        with open(DATA_FILE, 'r') as data_file:
            tasks = json.load(data_file)
            return [Task.from_dict(task) for task in tasks]
    except FileNotFoundError:
        return []
        
def save_task(task_list):
    task_dict = [task.to_dict() for task in task_list]
    with open(DATA_FILE, 'w') as data_file:
        json.dump(task_dict, data_file, indent=2)
    
    show_data(task_dict)

def task_exist(id):
    task_list = load_tasks()
    tasks_dict = [ task.to_dict() for task in task_list if task.id == int(id)]
    return bool(len(tasks_dict) > 0)

def add_task(description, status='TODO'):
    task_list = load_tasks()
    id = next_id([task.to_dict() for task in task_list])
    task_list.append(Task(id, description=description, status=status))
    save_task(task_list)
    print(f"Task {description} added successfully (ID={id})")

def next_id(list_dict):
    res = defaultdict(int)
    for task in list_dict :
        res['id'] = max(res['id'], task['id'])

    return int(res['id'])+1

def list_tasks(status):
    task_list = load_tasks()
    if bool(status and not status.isspace()):        
        return [ task.to_dict() for task in task_list if task.status == status]
    else: 
        return [ task.to_dict() for task in task_list]
    
def delete_task(id):
    task_list = [task for task in load_tasks() if task.id != int(id)]
    save_task(task_list)

def update_task(id, *args, **kwargs):
    task_list = load_tasks()
    index_list = [index for (index, item) in enumerate(task_list) if item.id == id]
    if len(index_list) > 0 :    
        index = index_list[0]
        for key, val in kwargs.items():
            if key == "description" :
                task_list[index].description = val
            if key == "status" :
                task_list[index].status = val
        
        task_list[index].updatedAt = datetime.datetime.now()
        
        save_task(task_list)
    else :
        print(f"Task with id {id} does not exist")

def show_data(data):
    df = pd.DataFrame.from_dict(data)
    print("\n")
    print(df)
    print("\n")


if __name__ == '__main__':
    task_list = load_tasks()
    list_dict = [task.to_dict() for task in task_list]
    