from task_cli.repositories.json_repository import JSONRepository
from task_cli.entities.task import Task
import builtins
import json
import pytest
import pandas as pd

MOCK_DATA = """[{\"id\":1, \"description\":\"TEST 1\", \"status\":\"TODO\", 
                    \"created_at\": \"2025-03-24 00:00:00\", \"updated_at\": \"2025-03-24 00:00:00\"},
                    {\"id\":2, \"description\":\"TEST 2\", \"status\":\"TODO\", 
                    \"created_at\": \"2025-03-24 00:00:00\", \"updated_at\": \"2025-03-24 00:00:00\"}]"""

MOCK_FILE = "fake_tasks.json"

@pytest.fixture
def mock_open(mocker):
    """Fixture to mock 'open' function"""
    return mocker.patch("builtins.open", mocker.mock_open()) 

@pytest.fixture
def json_repository():
    """Fixture Initialize JSONRepository with fake file."""
    return JSONRepository(MOCK_FILE)
    

def test_load_json_file(json_repository, mocker):
    """ Test to load tasks successfully"""
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data=MOCK_DATA))
    mocker.patch("json.load", return_value=json.loads(MOCK_DATA))

    tasks = json_repository.load_json_file()
    
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[0].description == "TEST 1"
    assert tasks[1].status == "TODO"
    mock_open.assert_called_once_with(MOCK_FILE, "r", encoding="utf-8")

def test_load_json_file_not_found(json_repository, mocker):
    """Test to load a non-existent JSON file """
    mocker.patch("builtins.open", side_effect=FileNotFoundError())

    tasks = json_repository.load_json_file()

    assert tasks == [] 

def test_save_json_file(json_repository, mock_open, mocker):
    """Test verify that the data is saved successfully in a JSON file."""
    mock_task = Task(_id=3, description="TEST SAVE", status="TODO")
    mock_json_dump = mocker.patch("json.dump")

    json_repository.save_json_file([mock_task])

    mock_open.assert_called_once_with(MOCK_FILE, "w", encoding="utf-8")
    mock_json_dump.assert_called_once_with(
        [mock_task.to_dict()], mock_open(), indent=2
    )

def test_show_data(json_repository):
    """Test to verify the dict list transformation to dataframe """

    df = json_repository.show_data(json.loads(MOCK_DATA))

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["id", "description", "status", "created_at", "updated_at"]