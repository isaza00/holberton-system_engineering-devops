#!/usr/bin/python3
""" fetch data from api and display it """

import json
import requests
import sys


if __name__ == "__main__":
    api_todos = "https://jsonplaceholder.typicode.com/users/"\
                + sys.argv[1] + "/todos"
    api_user = "https://jsonplaceholder.typicode.com/users/"\
               + sys.argv[1]
    file_name = sys.argv[1] + ".json"
    lista = []
    r1 = requests.get(api_todos)
    r2 = requests.get(api_user)
    for item in r1.json():
        lista.append({"task": item.get("title"),
                      "completed": item.get("completed"),
                      "username": r2.json().get("username")})
    dic = {sys.argv[1]: lista}
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(dic))
