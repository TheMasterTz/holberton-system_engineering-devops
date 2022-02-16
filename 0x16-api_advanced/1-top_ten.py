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
        params={'limit': '10'})

    if req.status_code in [404, 302]:
        print("None")
    else:
        json = req.json()
        if json.get('data') and json.get('data').get('children'):
            posts = json.get('data').get('children')

            for post in posts:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
