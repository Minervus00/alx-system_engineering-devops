#!C:/Users/LENOVO/anaconda3/python.exe
# /usr/bin/python3
"""Script that gather data from an api"""

if __name__ == "__main__":
    import requests
    from sys import argv

    userId = argv[1]

    url_v = 'https://jsonplaceholder.typicode.com/users/' + userId
    userInfo = requests.get(url_v).json()

    url_v = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(url_v).json()
    lst = []
    for td in todos:
        if td.get("userId") == userInfo.get("id"):
            lst.append({
                "task": td.get("title"),
                "completed": td.get("completed"),
                "username": userInfo.get("username")}
                )

    filename = str(userId) + ".json"
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(str({str(userId): lst}))
