#!/usr/bin/python3
"""
This function return number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Reutnr value if exists, else 0
    """
    headers = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get('https://www.reddit.com/r/{}/about.json'.
                            format(subreddit), headers=headers)
    if (response.status_code == 200):
        for key, value in response.json()['data'].items():
            if (key == 'subscribers'):
                return value
    return 0
