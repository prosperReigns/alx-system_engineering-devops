#!/usr/bin/python3

import requests
import sys

api_url = 'https://jsonplaceholder.typicode.com/todos/1'
employee_id = sys.argv[1]
response = requests.get(api_url + "user/{}".format(employee_id))
employee = response.json()

params = {"userId": employee_id}
todos = requests.get(api_url + "todos", params).json()

completed = [title.get("title") for title in todos if
                 title.get('completed') is True]

print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))

[print("\t {}".format(complete)) for complete in completed]


