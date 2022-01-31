#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    peticion = requests.get('{}users'.format(url)).json()

    with open('todo_all_employees.json', 'w') as f:
        json.dump({
            u.get("id"): [{
                "task": t.get('title'),
                "completed": t.get('completed'),
                "username": u.get('name')
            } for t in requests.get(url + "todos",
                                    params={
                                        "userId": u.get("id")
                                    }).json()]
            for u in peticion}, f)
