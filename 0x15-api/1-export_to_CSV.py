#!/usr/bin/python3

import requests
import csv
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user: int = argv[1]
    peticion = requests.get('{}users/{}'.format(url, user)).json()
    name = peticion.get('username')
    taskall = requests.get('{}todos'.format(url)).json()


    filename = user + '.csv'
    with open(filename, mode='w') as File:
        writer = csv.writer(File, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in taskall:
            if task.get('userId') == user:
                writer.writerow([user, name, str(task.get('completed')), task.get('title')])
