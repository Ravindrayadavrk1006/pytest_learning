import pytest
import source.service as service
import requests
import unittest.mock as mock

#mock is used for returning custom values when a function is being called which is described in the mock.patch and then checking against it
@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    username = service.get_user_from_db(1)
    
    assert username == "Mocked Alice"

@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "John Doe"
    }
    mock_get.return_value = mock_response
    data = service.get_user()
    assert data == {
        "id": 1,
        "name": "John Doe"
    }

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        data = service.get_user() 
        assert True