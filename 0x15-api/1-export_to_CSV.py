#!/usr/bin/python3
"""Script that gather data from an api"""

if __name__ == "__main__":
    import requests
    from sys import argv

    userId = argv[1]

    url_v = 'https://jsonplaceholder.typicode.com/users/' + userId
    userInfo = requests.get(url_v).json()

    url_v = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(url_v, params={"userId": userId}).json()

    filename = str(userId) + ".csv"
    with open(filename, 'a', encoding='utf-8') as f:
        for td in todos:
            f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                userId,
                userInfo.get("username"),
                td.get("completed"),
                td.get("title")
                )
            )
