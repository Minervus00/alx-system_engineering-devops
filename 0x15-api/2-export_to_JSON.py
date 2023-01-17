#!/usr/bin/python3
"""Script that gather data from an api"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    userId = argv[1]

    url_v = 'https://jsonplaceholder.typicode.com/users/' + userId
    userInfo = requests.get(url_v).json()

    url_v = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(url_v, params={"userId": userId}).json()
    lst = []
    for td in todos:
        lst.append({
            "task": td.get("title"),
            "completed": td.get("completed"),
            "username": userInfo.get("username")}
            )

    filename = str(userId) + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({userId: lst}, f)
