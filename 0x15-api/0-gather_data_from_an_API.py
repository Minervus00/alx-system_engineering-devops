#!/usr/bin/python3
"""Script that gather data from an api"""

if __name__ == "__main__":
    import requests
    from sys import argv

    userId = argv[1]

    url_v = 'https://jsonplaceholder.typicode.com/users/' + userId
    userInfo = requests.get(url_v).json()

    url_v = 'https://jsonplaceholder.typicode.com/todos'
    userTodos = requests.get(url_v, params={"userId": userId}).json()
    cptd = []
    for td in userTodos:
        if td.get("completed"):
            cptd.append(td)
    print("Employee {} is done with tasks({}/{}):".format(
        userInfo.get("name"),
        len(cptd),
        len(userTodos)
    ))
    for td in cptd:
        print("\t {}".format(td.get("title")))
