#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    # Set the Default URL strings
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    # Get the Response of the Reddit API
    request = requests.get(url).json()
    subs = request.get("data", {}).get("subscribers", 0)
    return subs
