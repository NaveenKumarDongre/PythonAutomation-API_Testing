import requests, json 


# GET API call return data
def getAPIData(url):
    headers = {'Content-Type': 'application/json'}
    print(f"Request URL: {url}")
    response = requests.get(url, headers=headers, verify=False)
    data = response.json() 
    assert len(data) > 0, "Empty response!"
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

# POST API call return data
def postAPIData(url, body):
    headers = {'Content-Type': 'application/json'}
    print(f"Request URL: {url}")
    print(f"Request Body: {json.dumps(body)}")
    response = requests.post(url, headers=headers, data=json.dumps(body), verify=False)
    data = response.json() 
    assert len(data) > 0, "Empty response!"
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

# PUT API call
def putAPIData(url, body):
    headers = {'Content-Type': 'application/json'} 
    print(f"Request URL: {url}")
    print(f"Request Body: {json.dumps(body)}")
    response = requests.put(url, headers=headers, data=json.dumps(body), verify=False) 
    data = response.json() 
    assert len(data) > 0, "Empty response!"
    timeTaken = response.elapsed.total_seconds()
    return  data, response.status_code, timeTaken 

# DELETE  API call 
def deleteAPIData(url, optHeader=None):
    headers = {'Content-Type': 'application/json'}
    print(f"Request URL: {url}")
    headers = (headers | optHeader) if isinstance(optHeader, dict) else headers
    response = requests.delete(url, headers=headers, verify=False)
    print(response.request.headers)
    data = response.json()
    assert len(data) > 0, "Empty response!"
    timeTaken = response.elapsed.total_seconds()
    return  data, response.status_code, timeTaken 
    




