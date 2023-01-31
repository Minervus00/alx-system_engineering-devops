#!/usr/bin/python
"""Module doculentation"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the total number of suscribers for a given subreddit"""
    resp = requests.get(
        'https://www.reddit.com/r/' + subreddit + '/top.json?limit=2',
        headers={'User-agent': 'yourbot'}).json()
    # print(resp)
    data = resp.get('data', None)
    print(data['children'][0]['data']['subreddit_subscribers'])
    if data is not None:
        return (data['children'][0]['data']['subreddit_subscribers'])
    else:
        return (0)
