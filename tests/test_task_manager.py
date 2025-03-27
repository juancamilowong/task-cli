"""
Tests for TaskManager using pytest-mock.
"""

import pytest
import datetime
from task_cli.services.task_manager import TaskManager
from task_cli.entities.task import Task
from task_cli.repositories.json_repository import JSONRepository


@pytest.fixture
def mock_repository(mocker):
    """Mock JSONRepository."""
    return mocker.MagicMock(spec=JSONRepository)

@pytest.fixture
def task_manager(mock_repository):
    """Instance of TaskManager."""
    return TaskManager(repository=mock_repository)

@pytest.fixture
def sample_tasks():
    """Mock Task list."""
    return [Task(1, "TEST 1", "DONE"), Task(2, "TEST 2", "TODO")]

def test_next_id(task_manager, sample_tasks):
    """Verify that next_id() returns the correct next ID"""
    assert task_manager.next_id([task.to_dict() for task in sample_tasks]) == 3

def test_task_exist(task_manager, mock_repository, sample_tasks):
    """Verify that task_exist() detects an existing task."""
    mock_repository.load_json_file.return_value = sample_tasks
    assert task_manager.task_exist(1) is True
    assert task_manager.task_exist(99) is False

def test_add_task(task_manager, mock_repository, mocker):
    """Verify that add_task() successfully adds a task."""
    mock_repository.load_json_file.return_value = []
    mock_repository.save_json_file = mocker.MagicMock()

    task_manager.add_task("New Task")

    mock_repository.save_json_file.assert_called_once()
    saved_tasks = mock_repository.save_json_file.call_args[0][0]
    assert len(saved_tasks) == 1
    assert saved_tasks[0].description == "New Task"

def test_list_tasks(task_manager, mock_repository, sample_tasks):
    """Verify that list_tasks() returns all or filtered tasks."""
    mock_repository.load_json_file.return_value = sample_tasks

    all_tasks = task_manager.list_tasks("")
    assert len(all_tasks) == 2

    done_tasks = task_manager.list_tasks("DONE")
    assert len(done_tasks) == 1
    assert done_tasks[0]["status"] == "DONE"

def test_delete_task(task_manager, mock_repository, mocker, sample_tasks):
    """Verify that delete_task() correctly deletes a task."""
    mock_repository.load_json_file.return_value = sample_tasks
    mock_repository.save_json_file = mocker.MagicMock()

    task_manager.delete_task("1")

    mock_repository.save_json_file.assert_called_once()
    remaining_tasks = mock_repository.save_json_file.call_args[0][0]
    assert len(remaining_tasks) == 1
    assert remaining_tasks[0].id == 2

def test_update_task(task_manager, mock_repository, mocker, sample_tasks):
    """Verify that update_task() correctly updates a task."""
    mock_repository.load_json_file.return_value = sample_tasks
    mock_repository.save_json_file = mocker.MagicMock()

    task_manager.update_task("1", description="Updated Task", status="IN_PROGRESS")

    mock_repository.save_json_file.assert_called_once()
    updated_tasks = mock_repository.save_json_file.call_args[0][0]
    updated_task = next(t for t in updated_tasks if t.id == 1)
    assert updated_task.description == "Updated Task"
    assert updated_task.status == "IN_PROGRESS"
    assert isinstance(updated_task.updated_at, datetime.datetime)

def test_show_task_table(task_manager, mock_repository, sample_tasks, mocker):
    """Verify that show_task_table() calls show_data() correctly."""
    mock_repository.load_json_file.return_value = sample_tasks
    mock_repository.show_data = mocker.MagicMock()

    task_manager.show_task_table("TODO")

    mock_repository.show_data.assert_called_once()    