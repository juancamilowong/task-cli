"""
Command line CLI to task tracking
"""

import cmd
import shlex
from tasks import (
    add_task,
    delete_task,
    list_tasks,
    show_data,
    update_task,
    task_exist
)

valid_status = ["TODO", "IN-PROGRESS", "DONE"]
VALID_ID_MESSAGE = "Please, use a valid ID"


class TaskCLI(cmd.Cmd):
    """Task cli class command prompt class"""

    intro = """Welcome to the task tracker, I am glad to help you with them.
    
    You can type help to check the valid commands.
    """
    #pylint: disable=unused-argument
    def do_greet(self, arg):
        """Greeting method"""
        print("Hello, I am here to help with your keep track of your tasks")
    #pylint: disable=unused-argument, invalid-name)
    def do_EOF(self, arg):
        """EOF"""
        return True
    #pylint: disable=unused-argument
    def do_help(self, arg):
        """Show help information"""
        print(
            """
            - Add new tasks: add <decription>
            - List all tasks: list
            - List by status: list <DONE|TODO|IN-PROGRESS>
            - Update task description: update <id> <description>
            - Delete task: delete <id>
            - Mark task IN-PROGRESS:  mark_in_progress <id>
            - Mark task DONE:  mark_done <id>
"""
        )
    #pylint: disable=unused-argument
    def do_quit(self, arg):
        """Exit command prompt"""
        print("Exiting the console")
        return True
    #pylint: disable=unused-argument
    def do_exit(self, arg):
        """Exit command prompt"""
        print("Exiting the console")
        return True

    def do_add(self, description):
        """Ass task"""
        add_task(description=description.strip('"'))

    def do_list(self, status):
        """List tasks"""
        show_data(list_tasks(status))

    def do_delete(self, _id):
        """Delete task"""
        if not _id.isnumeric() :
            print(VALID_ID_MESSAGE)
            return
        if task_exist(_id):
            delete_task(_id)
        else:
            print(f"Task with id {_id} does not exist")

    def do_update(self, args):
        """Update task"""
        args = shlex.split(args)

        if len(args) < 2:
            print(
                "Please type the correct arguments to update : update <id> <description>"
            )
        else:
            if not args[0].isnumeric() :
                print(VALID_ID_MESSAGE + " in position 1")
                return
            task_id = int(args[0])
            description = args[1]

            update_task(task_id, description=description)

    def do_mark_in_progress(self, _id):
        """Mark task status IN-PROGRESS"""
        if not _id.isnumeric() :
            print(VALID_ID_MESSAGE)
            return
        update_task(int(_id), status="IN-PROGRESS")

    def do_mark_done(self, _id):
        """Mark task status DONE"""
        if not _id.isnumeric() :
            print(VALID_ID_MESSAGE)
            return
        update_task(int(_id), status="DONE")


if __name__ == "__main__":
    TaskCLI().cmdloop()
