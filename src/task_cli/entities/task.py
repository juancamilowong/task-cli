"""
Task Entity Module.

Defines the Task dataclass, which represents a single task entity.
"""

import datetime
from typing import Dict

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class Task:
    """Task definition class"""

    # pylint: disable=too-many-arguments, too-many-positional-arguments, redefined-builtin
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
    def from_dict(cls, task_dict: Dict[str, str]):
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
