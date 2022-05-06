from urllib import response
import requests
import json

def test_api():
    url = requests.get("https://reqres.in/api/users?page=1")
    assert url.status_code == 200

    data_json = json.dumps(url.json())
    print(data_json)

    for particular_data in url.json()['data']:
        if particular_data['id'] == 1:
            assert particular_data['first_name'] == 'George'
            assert particular_data['last_name'] == 'Bluth'
            print("Information Matched!!!")
        else:
            print("Information not matched")
