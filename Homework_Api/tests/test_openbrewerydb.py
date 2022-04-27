import pytest
import requests

base_url = "https://api.openbrewerydb.org"


@pytest.mark.parametrize("state", ["Nebraska", "New York"])
def test_by_city(state):
    response = requests.get(url=base_url + "/breweries?by_city=" + state)
    for item in response.json():
        assert item["state"] == state


def test_quantity():
    quantity = 5
    response = requests.get(url=base_url + "/breweries?per_page=" + str(quantity))
    assert len(response.json()) == quantity


def test_breweries_url():
    response = requests.get(url=base_url + "/breweries")
    assert response.status_code == 200


@pytest.mark.parametrize("b_type", ["micro", "nano"])
def test_type(b_type):
    response = requests.get(url=base_url + "/breweries?by_type=" + b_type)
    for item in response.json():
        assert item["brewery_type"] == b_type


def test_dog_name():
    response = requests.get(url=base_url + "/breweries/autocomplete?query=dog")
    for item in response.json():
        assert "dog" in item["name"].lower()
