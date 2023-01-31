#!/usr/bin/python3
"""Module doculentation"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of suscribers for a given subreddit"""
    resp = requests.get(
        'https://www.reddit.com/r/' + subreddit + '/top.json?limit=2',
        headers={'User-agent': 'yourbot'}).json()
    data = resp.get('data', None)
    if data is not None:
        child = data['children']
        if child:
            return (child[0]['data']['subreddit_subscribers'])
    return (0)
