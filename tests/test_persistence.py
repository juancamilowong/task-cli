from task_cli.repositories.json_repository import Task, load_json_file, DATA_FILE, save_json_file, task_exist
import builtins
import json
import pytest

MOCKED_JSON = [{"id":1, "description":"TEST 1", "status":"TODO", 
                    "created_at": "2025-03-24 00:00:00", "updated_at": "2025-03-24 00:00:00"},
                    {"id":2, "description":"TEST 2", "status":"TODO", 
                    "created_at": "2025-03-24 00:00:00", "updated_at": "2025-03-24 00:00:00"}]

def test_load_json_file(mocker):
    
    json_content = json.dumps(MOCKED_JSON)

    # Mock 'open' method
    mock_open = mocker.mock_open(read_data=json_content)
    mocker.patch.object(builtins, 'open', mock_open) 

    json_list = [task.to_dict() for task in load_json_file()]

    # Check Json load
    assert json_list == MOCKED_JSON
    mock_open.assert_called_once_with(DATA_FILE,'r', encoding='utf-8')

def test_save_json_file(mocker):

    json_content = json.dumps(MOCKED_JSON)
    
    mock_open = mocker.mock_open(read_data=json_content)
    mocker.patch.object(builtins, 'open', mock_open) 

    task_list = [Task.from_dict(task) for task in MOCKED_JSON]
    save_json_file(task_list)

    mock_open.assert_called_once_with(DATA_FILE,'w', encoding='utf-8')

def test_task_exist(mocker):
    
    json_content = json.dumps(MOCKED_JSON)

    # Mock 'open' method
    mock_open = mocker.mock_open(read_data=json_content)
    mocker.patch.object(builtins, 'open', mock_open)

    assert task_exist(1)
    assert not task_exist(4)