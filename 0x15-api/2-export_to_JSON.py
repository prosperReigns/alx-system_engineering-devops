#!/usr/bin/python3
"""  script to export data in the JSON format. """

import json
import requests
import sys


user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"

user = requests.get(url + "users/{}".format(user_id)).json()
username = user.get("username")

params = {"userId": user_id}
todos = requests.get(url + "todos", params).json()


data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }
with open("{}.json".format(user_id), "w") as jsonfile:
    json.dump(data_to_export, jsonfile, indent=4)
