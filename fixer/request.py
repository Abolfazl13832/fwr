import json
import requests

def get_request(url:str):
    response = requests.get(url)
    if response.status_code == 200 :
        return json.loads(response.text)
    return None
