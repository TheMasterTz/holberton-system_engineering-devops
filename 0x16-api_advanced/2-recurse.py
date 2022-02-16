#!/usr/bin/python3
"""
    Module for task 2
"""
import requests


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """

    