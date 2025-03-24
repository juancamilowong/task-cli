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
- pandas
- pylint
- black[jupyter]
- pytest
- pytest-mock
- coverage
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

### Add 
Add new tasks in TODO status

```
add "New task"
```

### List
List all your taks or list by status

```
list
```
or
```
list TODO
```
### Update 
Update tasks descriptions

```
update 1 "Updated description"
```

### Mark 
Mark your tak status as "IN-PROGRESS" or "DONE" using id
```
mark_in_progress 2
```

```
mark_done 2
```
### Delete 

Remove task using id
```
delete 1
```

### Help
Show all the commands
```
help
```
## Contributors

- [@juancamilowong](https://www.github.com/juancamilowong)

## Project source

This is a project from [Roadmap](https://www.roadmap.sh). Click this [link](https://roadmap.sh/projects/task-tracker) to checkout the project