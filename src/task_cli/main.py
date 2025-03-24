"""
Command line CLI to task tracking
"""

import sys
import os
import cmd
import shlex
from task_cli.services.task_manager import TaskManager
from task_cli.repositories.json_repository import JSONRepository

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
DATA_FILE = "task_list.json"


class TaskCLI(cmd.Cmd):
    """Command line class"""

    json_repository = JSONRepository(DATA_FILE)
    task_manager = TaskManager(json_repository)
    """Task cli class command prompt class"""

    intro = "Welcome to the task tracker, Type help or ? to list commands"
    prompt = "task-cli > "

    # pylint: disable=unused-argument
    def do_bye(self, arg):
        """Exit command prompt"""
        print("Thank you for using task-cli")
        return True

    def do_add(self, description):
        """
        Add new task
        
        Args:
         description (str): Task description

        Returns:
            None
        """
        self.task_manager.add_task(description)

    def do_list(self, status):
        """
        List all tasks or filteres by status

        Args:
         status (str, optional): status of the task
        
        Returns:
            None
        """
        self.task_manager.show_task_table(status)

    def do_delete(self, _id):
        """
        Delete task by id
        
        Args:
         _id (int): task id
        
        Returns:
            None
        """
        self.task_manager.delete_task(_id)

    def do_update(self, args):
        """
        Update task decription by id
        
        Args:
         _id (int): Task id
         description (str): New task description
        
        Returns:
            None

        """
        args = shlex.split(args)

        if len(args) < 2:
            print(
                "Please type the correct arguments to update : update <id> <description>"
            )
        else:
            self.task_manager.update_task(args[0], description=args[1])

    def do_mark_in_progress(self, _id):
        """
        Mark task status IN-PROGRESS

        Args:
         _id (int): task id
        
        Returns:
            None
        """
        self.task_manager.update_task(_id, status="IN-PROGRESS")

    def do_mark_done(self, _id):
        """
        Mark task status DONE
        
        Args:
         _id (int): task id
        
        Returns:
            None
        """
        self.task_manager.update_task(_id, status="DONE")


def main():
    """Main methos initialize command line"""
    TaskCLI().cmdloop()
