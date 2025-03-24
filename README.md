# TASK TRACKER CLI

This task tracker allows you to add, update and change the status of your daily tasks

- [TASK TRACKER CLI](#task-tracker-cli)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Initialization](#initialization)
    - [Add](#add)
    - [List](#list)
    - [Update](#update)
    - [Mark](#mark)
    - [Delete](#delete)
    - [Help](#help)
  - [Contributors](#contributors)
  - [Project source](#project-source)

## Prerequisites

Before you begin ensure you have the following installed:

- Python 3.10 or higher
- Pandas
- an accessible terminal

## Installation

1. Clone repository
```bash
git clone https://github.com/tu-usuario/task_cli.git
cd task_cli
```
2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
```
3. Install the module 
```bash
pip install -e .
```
## Usage

### Initialization
Initialization command to run the CLI
```
task_cli
```
![Initialization screenshot](Images/initialization.png)

### Add 
Add new tasks in TODO status

ARGS:
- description
```
add "New task"
```
![add screenshot](Images/add.png)
### List
List all your taks or list by status

ARGS:
- status or blank (list all)

```
list
```
![list screenshot](Images/list.png)
```
list TODO
```
![list status screenshot](Images/list-todo.png)
### Update 
Update tasks descriptions

ARGS:
- id
- description
```
update 1 "Updated description"
```
![update screenshot](Images/update.png)
### Mark 
Mark your tak status as "IN-PROGRESS" or "DONE" using id

ARGS:
- id
```
mark_in_progress 2
```
![mark-in-progress screenshot](Images/mip.png)
```
mark_done 3
```
![mark-done screenshot](Images/md.png)
### Delete 

Remove task using id

ARGS:
- id
```
delete 1
```
![delete screenshot](Images/md.png)

### Help
Show all the commands and their arguments
```
help
```
![help screenshot](Images/help.png)

## Contributors

- [@juancamilowong](https://www.github.com/juancamilowong)

## Project source

This is a project from [Roadmap](https://www.roadmap.sh). Click this [link](https://roadmap.sh/projects/task-tracker) to checkout the project