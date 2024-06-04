#!/usr/bin/python3
""" a script to export data in the CSV format. """

import requests
import sys
import csv


api_url = 'https://jsonplaceholder.typicode.com/todos/1'
employee_id = sys.argv[1]
response = requests.get(api_url + "user/{}".format(employee_id))
employee = response.json()
username = employee.get("sername")

params = {"userId": employee_id}
todos = requests.get(api_url + "todos", params).json()

completed = [title.get("title") for title in todos if
    title.get('completed') is True]

with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    [writer.writerow(
        [user_id, username, todo.get("completed"), todo.get("title")]
    ) for todo in todos]
