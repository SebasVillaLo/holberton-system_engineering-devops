#!/usr/bin/python3
"""
This script is for get the name and finished task of the empleate
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'
    user: int = argv[1]
    peticion = requests.get('{}users/{}'.format(url, user)).json()
    name = peticion.get('name')
    taskall = requests.get('{}todos?userId={}'.format(url, user)).json()

    taskList = []
    for task in taskall:
        if task.get('completed') is True:
            taskList.append(task.get('title'))

    print("Employee {} is done with tasks({}/{})"
          .format(name, len(taskList), len(taskall)))
    print("\n".join('\t {}'.format(task) for task in taskList))
