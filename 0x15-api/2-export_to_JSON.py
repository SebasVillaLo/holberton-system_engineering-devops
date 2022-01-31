#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = int(argv[1])
    peticion = requests.get('{}users/{}'.format(url, user)).json()
    taskall = requests.get('{}todos?userId={}'.format(url, user)).json()

    filename = "{}.json".format(user)

    with open(filename, 'w') as f:
        json.dump({user: [{
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": t.get('username')
        } for t in taskall]}, f)
