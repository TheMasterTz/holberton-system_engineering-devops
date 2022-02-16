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
                     headers={'User-Agent': 'Python/requests'},
                     params={'limit': 10})
    if req.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in req.json().get("data").get("children")]
