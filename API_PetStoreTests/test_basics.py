import requests
import json


baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '151'


# Post a pet with a particular ID
def test_postPetByID_response():
    url = baseURI

    request_body = {
        "id": petID,
         "name": "Cutie",
        "status": "available"
    }
    header = {'Content-Type': 'application/json'}
    print(f"Request URL: {url}")

    # HTTP post method
    response = requests.post(
        url, verify=True, json=request_body, headers=header)
    data = response.json()
    print(json.dumps(data, indent=2))

    assert response.status_code == 200

# test valid response is not empty


def test_getPetById_response():
    url = baseURI + petID
    header = {'Content-Type': 'application/json'}
    print(f"Request URL: {url}")

    # HTTP get method
    response = requests.get(url, verify=True, headers=header)
    data = response.json()
    print(json.dumps(data, indent=2))

    assert len(data) > 0, "Empty response!"


# test response body for "ID" key
def test_getPetByID_id():
    url = baseURI + petID
    header = {'Content-Type': 'application/json'}
    print(f"Request URL: {url}")

    # HTTP get method
    response = requests.get(url, verify=True, headers=header)
    data = response.json()
    print(json.dumps(data, indent=2))

    assert data['id'] == 151


# def test_deletePetByID_id():
#     url = baseURI + petID
#     header = {'Content-Type': 'application/json', 'api_key': 'navin'}
#     print(f"Request URL: {url}")

#     # HTTP delete method
#     response = requests.delete(url, verify=True, headers=header)
#     data = response.json()
#     print(json.dumps(data, indent=2))

#     assert response.status_code == 200
