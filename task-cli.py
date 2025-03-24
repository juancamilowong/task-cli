import cmd
import shlex
import tasks

valid_status = ["TODO", "IN-PROGRESS", "DONE"]


class TaskCLI(cmd.Cmd):
    intro = """Welcome to the task tracker, I am glad to help you with them.
    
    You can type help to check the valid commands.
    """

    def do_greet(self, arg):
        print("Hello, I am here to help with your keep track of your tasks")

    def do_EOF(self, arg):
        return True

    def do_help(self, arg):
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

    def do_quit(self, arg):
        print("Exiting the console")
        return True

    def do_exit(self, arg):
        print("Exiting the console")
        return True

    def do_add(self, description):
        tasks.add_task(description=description.strip('"'))

    def do_list(self, status):
        tasks.show_data(tasks.list_tasks(status))

    def do_delete(self, id):
        if tasks.task_exist(id):
            tasks.delete_task(id)
        else:
            print(f"Task with id {id} does not exist")

    def do_update(self, args):
        args = shlex.split(args)

        if len(args) < 2:
            print(
                "Please type the correct arguments to update : update <id> <description>"
            )
        else:
            task_id = int(args[0])
            description = args[1]

            tasks.update_task(task_id, description=description)

    def do_mark_in_progress(seld, id):
        tasks.update_task(int(id), status="IN-PROGRESS")

    def do_mark_done(seld, id):
        tasks.update_task(int(id), status="DONE")


if __name__ == "__main__":
    TaskCLI().cmdloop()
