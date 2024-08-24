from utils.myutils  import getAPIData, putAPIData, postAPIData, deleteAPIData
from utils.myConfigParser import  getPetAPIURL
import json

baseURI = getPetAPIURL()
petID = '151'

# creating a new pet with petID = '151'
def test_postPet_response():
    url = baseURI 
    payload =  {
        "id": 151,
        "name": "Cutie",
        "status":  "available"
    }
    res = postAPIData(url, payload)
    data, statusCode, timeTaken = res[0], res[1], res[2] 
    print(json.dumps(data, indent=2))
    assert  statusCode ==  200, f"Expected status code to be 200 but got {statusCode}"
    print(f"Status code: {statusCode}")
    print(f"Total time taken: {timeTaken}") 
    assert data['id'] == int(petID)  , f"Expected id to be {petID} but got {data['id']}"

def test_getPetById_response():
    url = baseURI + petID 
    data, statusCode, timeTaken  = getAPIData(url)[0], getAPIData(url)[1], getAPIData(url)[2]
    print(json.dumps(data, indent=2))
    assert statusCode  == 200, f"Expected status code to be 200 but got {statusCode}"
    print(f"Status code: {statusCode}")
    print(f"Total time taken: {timeTaken}")
    assert data['id'] == int(petID)  , f"Expected id to be {petID} but got {data['id']}"

def test_updatePet_response():
    payload = {
        "id": int(petID),
        "name": "Cutie Pie",
        "status": "pending"
    }
    res =  putAPIData(baseURI, payload)
    data,  statusCode, timeTaken  = res[0], res[1], res[2] 
    print(json.dumps(data, indent=2))
    assert statusCode ==  200, f"Expected status code to be 200 but got {statusCode}"
    print(f"Status code: {statusCode}")
    print(f"Total time taken: {timeTaken}")

def test_deletePet_response():
    url = baseURI + petID 
    apiKey = {'api_key':'apiKeys123'} 

    res = deleteAPIData(url, apiKey) 
    data,  statusCode, timeTaken = res[0], res[1], res[2]  
    print(json.dumps(data, indent=2))
    assert  statusCode == 200, f"Expected status code to be 200 but got {statusCode}"
    print(f"Status code: {statusCode}")
    assert data['message'] == petID,  f"Expected message to be {petID} but got {data['message']}"
    print(f"Total time taken: {timeTaken}")


    

