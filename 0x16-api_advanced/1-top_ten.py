#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """prints the titles of the top ten hot posts for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
    req = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     headers={'User-Agent': 'MyHolbertonAPI/0.0.1'})
    if req.status_code == 200:
        content = req.json()
        children = content['data']['children']
        for child in children:
            print(child['data']['title'])
    else:
        print(None)
