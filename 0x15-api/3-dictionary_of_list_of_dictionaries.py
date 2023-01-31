#!/usr/bin/python3
"""Script that gather data from an api"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    data = {}
    usernames = {}

    url_v = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url_v).json()
    for user in users:
        usernames[str(user["id"])] = user["username"]
        data[str(user["id"])] = []

    url_v = 'https://jsonplaceholder.typicode.com/todos/'
    todos = requests.get(url_v).json()
    lst = []
    for td in todos:
        data[str(td["userId"])].append({
            "task": td.get("title"),
            "completed": td.get("completed"),
            "username": usernames[str(td["userId"])]}
            )

    with open("todo_all_employees.json", 'w', encoding='utf-8') as f:
        json.dump(data, f)
