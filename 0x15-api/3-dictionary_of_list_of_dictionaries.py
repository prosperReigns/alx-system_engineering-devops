#!/usr/bin/python3
""" script to export data in the JSON format. v"""

import json
import requests


url = "https://jsonplaceholder.typicode.com/"
users = requests.get(url + "users").json()

with open("todo_all_employees.json", "w") as jsonfile:
    json.dump({
        u.get("id"): [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": u.get("username")
        } for t in requests.get(url + "todos",
                                params={"userId": u.get("id")}).json()]
        for u in users}, jsonfile)
