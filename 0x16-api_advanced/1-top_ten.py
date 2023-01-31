#!/usr/bin/python3
"""Module doculentation"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed
    for a given subreddit"""
    resp = requests.get(
        'https://www.reddit.com/r/' + subreddit + '/top.json?limit=10',
        headers={'User-agent': 'yourbot'}).json()
    # print(resp)
    data = resp.get('data', None)
    # print(data['children'][0]['data']['subreddit_subscribers'])
    if data is not None:
        child = data['children']
        # print(child)
        for ch in child:
            print(ch['data']['title'])
        if child:
            return
    print(None)
