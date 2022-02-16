#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """prints the titles of the top ten hot posts for a given subreddit"""

    req = requests.get(
        'http://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={'User-Agent': 'Python/requests'},
        params={'limit': '10'}).json()

    posts = req.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data', {}).get('title', None))
