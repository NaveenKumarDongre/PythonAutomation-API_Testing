from utils.myutils import getAPIData, putAPIData, postAPIData, deleteAPIData
from utils.myConfigParser import getPetAPIURL
import json
import logging 

# Configure the logger
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

baseURI = getPetAPIURL()
petID = '151'

# Creating a new pet with petID = '151'
def test_postPet_response():
    url = baseURI
    payload = {
        "id": 151,
        "name": "Cutie",
        "status": "available"
    }
    LOGGER.info("Starting POST request to create a new pet with ID %s", petID)
    try:
        res = postAPIData(url, payload)
        LOGGER.info("API call done! Response received.")
        
        data, statusCode, timeTaken = res
        LOGGER.debug("Response data: %s", json.dumps(data, indent=2))
        assert statusCode == 200, f"Expected status code to be 200 but got {statusCode}"
        LOGGER.info("POST request successful with status code %s", statusCode)
        assert data['id'] == int(petID), f"Expected id to be {petID} but got {data['id']}"
        LOGGER.info("Pet ID verification successful.")
    except AssertionError as e:
        LOGGER.error("Assertion error occurred: %s", e)
        raise
    except Exception as e:
        LOGGER.exception("An error occurred during the POST request: %s", e)
        raise

def test_getPetById_response():
    url = baseURI + petID
    LOGGER.info("Starting GET request to retrieve pet with ID %s", petID)
    try:
        res = getAPIData(url)
        data, statusCode, timeTaken = res
        LOGGER.debug("Response data: %s", json.dumps(data, indent=2))
        assert statusCode == 200, f"Expected status code to be 200 but got {statusCode}"
        LOGGER.info("GET request successful with status code %s", statusCode)
        assert data['id'] == int(petID), f"Expected id to be {petID} but got {data['id']}"
        LOGGER.info("Pet ID verification successful.")
    except AssertionError as e:
        LOGGER.error("Assertion error occurred: %s", e)
        raise
    except Exception as e:
        LOGGER.exception("An error occurred during the GET request: %s", e)
        raise

def test_updatePet_response():
    payload = {
        "id": int(petID),
        "name": "Cutie Pie",
        "status": "pending"
    }
    LOGGER.info("Starting PUT request to update pet with ID %s", petID)
    try:
        res = putAPIData(baseURI, payload)
        data, statusCode, timeTaken = res
        LOGGER.debug("Response data: %s", json.dumps(data, indent=2))
        assert statusCode == 200, f"Expected status code to be 200 but got {statusCode}"
        LOGGER.info("PUT request successful with status code %s", statusCode)
    except AssertionError as e:
        LOGGER.error("Assertion error occurred: %s", e)
        raise
    except Exception as e:
        LOGGER.exception("An error occurred during the PUT request: %s", e)
        raise

def test_deletePet_response():
    url = baseURI + petID
    apiKey = {'api_key': 'apiKeys123'}

    LOGGER.info("Starting DELETE request to remove pet with ID %s", petID)
    try:
        res = deleteAPIData(url, apiKey)
        data, statusCode, timeTaken = res
        LOGGER.debug("Response data: %s", json.dumps(data, indent=2))
        assert statusCode == 200, f"Expected status code to be 200 but got {statusCode}"
        LOGGER.info("DELETE request successful with status code %s", statusCode)
        assert data['message'] == petID, f"Expected message to be {petID} but got {data['message']}"
        LOGGER.info("Pet deletion verification successful.")
    except AssertionError as e:
        LOGGER.error("Assertion error occurred: %s", e)
        raise
    except Exception as e:
        LOGGER.exception("An error occurred during the DELETE request: %s", e)
        raise
