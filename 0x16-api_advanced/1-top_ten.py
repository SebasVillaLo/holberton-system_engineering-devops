#!/usr/bin/python3
"""
Show in console the ten hot titles
"""

import requests


def top_ten(subreddit):
    """
    Return 0 if failed
    """
    count = 1
    headers = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get('https://www.reddit.com/r/{}/hot.json'.
                            format(subreddit), headers=headers)
    if (response.status_code == 200 and
            response.json()['data']['children'] != []):
        for value in response.json()['data']['children']:
            if (count <= 10):
                print(value['data']['title'])
                count += 1
            else:
                break
    else:
        print(None)
