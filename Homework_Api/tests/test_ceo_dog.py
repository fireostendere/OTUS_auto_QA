import pytest
import requests

from jsonschema import validate

base_url = "https://dog.ceo/api"


def test_bread_list():
    response = requests.get(url=base_url + "/breeds/list/all")
    assert response.status_code == 200


def test_schema():
    response = requests.get(url=base_url + "/breeds/image/random")

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize("breed", ["dane-great", "newfoundland"])
def test_bread(breed):
    response = requests.get(url=base_url + "/breed/" + breed + "/images")
    for item in response.json()["message"]:
        assert breed in item


@pytest.mark.parametrize("breed, is_sub_breed", [("hound", True), ("affenpinscher", False)])
def test_bread(breed, is_sub_breed):
    response = requests.get(url=base_url + "/breed/" + breed + "/list")
    if is_sub_breed:
        assert len(response.json()["message"]) > 0
    else:
        assert len(response.json()["message"]) == 0


def test_invalid_link():
    response = requests.get(url=base_url + "/qwertyytrewq")
    assert response.status_code == 404
