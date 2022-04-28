import requests


def test_task_4(url, status_code):
    response = requests.get(url=url["url"])
    assert str(response.status_code) == status_code["status_code"]
