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


def test_api_post():
    post_data = {'name': 'Allen', 'job': 'QA'}

    url = requests.post("https://reqres.in/api/users", data=post_data)
    
    post_data = url.json()
    assert url.status_code == 201
    assert post_data['name'] == 'Allen'
    assert post_data['job'] == 'QA'


